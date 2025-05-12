from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Opere, Categorie
from .models import Risposte, Domande, Quiz

# Create your views here.
def index(request):
    return render(request, "index.html")


def biografia(request):
    return render(request, "biografia.html")


def tvolt(request):
    return render(request, "tvolt.html")

def about(request):
    return render(request, "about.html")


def invenzioni(request):
    invenzioni = Opere.objects.all()
    opt = []
    for invenzione in invenzioni:
        opt.append(invenzione.titolo.lower())
    
    return render(request, "invenzioni.html", {"invenzioni": opt})


def details(request):
    invenzioni = Opere.objects.all()
    opt = []
    for invenzione in invenzioni:
        opt.append(invenzione.titolo.lower())
   
    selected = request.POST.get("invenzione").lower()
    opera_s = Opere.objects.filter(titolo=selected)
    desc = opera_s.descrizione
    data = opera_s.data
    titolo = opera_s.titolo
    categoria = Categorie.objects.filter(id=opera_s.id_categoria).nome
    autori =opera_s.autori_set.all()
    immagini = opera_s.immagini_set.all()

    return render(request, "details.html", {"invenzioni": opt, "invenzione": titolo, "descrizione": desc, "data": data, "categoria": categoria})

def gamification(request):
    return render(request, "gamification.html")

def game(request):
    session = request.session
    #session.clear()

    # Parametri GET
    categoria_quiz = request.GET.get("categoriaQuiz")
    if "categoria_quiz" not in request.session:
        # Imposto la sessione
        session["categoria_quiz"] = categoria_quiz
        session["domanda_selezionata"] = 0
    
    quiz = Quiz.objects.filter(categoria=session["categoria_quiz"])[0]
    domanda = Domande.objects.filter(id_quiz=quiz.pk)[session["domanda_selezionata"]]
    risposte_domanda = Risposte.objects.filter(id_domanda=domanda.pk)
    
    # Controllo se l'utente invia la risposta
    if request.method == "POST":
        risposta_selezionata = int(request.POST.get("risposta")[0]) - 1
        session["risposta_data"+str(session["domanda_selezionata"])] = risposte_domanda[risposta_selezionata].isRisposta
        session["domanda_selezionata"] += 1
    
    risposte_date = []

    for i in range(4):
        risposta_data_nome = "risposta_data"+str(i)
        risposte_date.append(None if risposta_data_nome not in session else session[risposta_data_nome] )
    return render(request, 'game.html', {"domanda": domanda, "risposte": risposte_domanda, "risposte_date": risposte_date})

def game_view(request):
    if 'domande_rimanenti' not in request.session:
        tutte = list(Domande.objects.values_list('id', flat=True))
        request.session['domande_rimanenti'] = tutte
        request.session['punteggio'] = 0

    domande_rimanenti = request.session['domande_rimanenti']

    if not domande_rimanenti:  #se le domande sono finite, da sistemare anche se sono state errate due domande. Bisogna anche fermare il gioco quando sono corrette almeno 3 risposte o si è arrivati a 4 risposte date
        punteggio = request.session.get('punteggio', 0)
        request.session.flush()
        return render(request, 'quiz/quiz.html', {
            'quiz_finito': True,
            'punteggio': punteggio,
        })

    id_domanda = domande_rimanenti[0]
    domanda = Domande.objects.get(id=id_domanda)
    risposte = domanda.risposte.all()

    if request.method == 'POST':
        risposta_id = int(request.POST.get('risposta'))
        risposta = Risposte.objects.get(id=risposta_id)
        
        if risposta.isRisposta:
            request.session['punteggio'] += 1
        
        domande_rimanenti.pop(0)
        request.session['domande_rimanenti'] = domande_rimanenti
        return redirect('game')

    return render(request, 'game/game.html', {'domanda': domanda, 'risposte': risposte})

'''def quiz(request):
    quizId = int(request.GET.get('quizId')) if request.GET.get('quizId') != None else None
    questionId = int(request.GET.get('questionId')) if request.GET.get('questionId') != None else None
    answerId = int(request.GET.get('answerId')) if request.GET.get('answerId') != None else None
    print(quizId, questionId, answerId)
    quizs = [
        {
            "id": 0,
            "categoria": "Test",
            "domande": [
                {
                    "id": 0,
                    "body": "Domanda test1",
                    "url_pagina": "/",
                    "risposte": [
                        {
                            "id": 0,
                            "body": "Risposta1",
                            "isRisposta": True,
                        },
                        {
                            "id": 1,
                            "body": "Risposta2",
                            "isRisposta": False,
                        },
                        {
                            "id": 2,
                            "body": "Risposta3",
                            "isRisposta": False,
                        },
                        {
                            "id": 3,
                            "body": "Risposta4",
                            "isRisposta": False
                        }
                    ]
                },
                {
                    "id": 1,
                    "body": "Domanda test2",
                    "url_pagina": "/",
                    "risposte": [
                        {
                            "id": 0,
                            "body": "Risposta1",
                            "isRisposta": False,
                        },
                        {
                            "id": 1,
                            "body": "Risposta2",
                            "isRisposta": True,
                        },
                        {
                            "id": 2,
                            "body": "Risposta3",
                            "isRisposta": False,
                        },
                        {
                            "id": 3,
                            "body": "Risposta4",
                            "isRisposta": False
                        }
                    ]
                },
                {
                    "id": 2,
                    "body": "Domanda test1",
                    "url_pagina": "/",
                    "risposte": [
                        {
                            "id": 0,
                            "body": "Risposta1",
                            "isRisposta": False,
                        },
                        {
                            "id": 1,
                            "body": "Risposta2",
                            "isRisposta": False,
                        },
                        {
                            "id": 2,
                            "body": "Risposta3",
                            "isRisposta": True,
                        },
                        {
                            "id": 3,
                            "body": "Risposta4",
                            "isRisposta": False
                        }
                    ]
                },
                {
                    "id": 3,
                    "body": "Domanda test4",
                    "url_pagina": "/",
                    "risposte": [
                        {
                            "id": 0,
                            "body": "Risposta1",
                            "isRisposta": False,
                        },
                        {
                            "id": 1,
                            "body": "Risposta2",
                            "isRisposta": False,
                        },
                        {
                            "id": 2,
                            "body": "Risposta3",
                            "isRisposta": False,
                        },
                        {
                            "id": 3,
                            "body": "Risposta4",
                            "isRisposta": False
                        }
                    ]
                }
            ]
        }
    ]

    if quizId == None:
        return JsonResponse({ "error": {
            "message": "quizId not provided",
        }})
    
    selectedQuiz = quizs[quizId]
    
    if questionId != None and answerId != None:
        correctAnswer = selectedQuiz["domande"][questionId]["risposte"][answerId]["isRisposta"]
        return JsonResponse({ "correctAnswer": correctAnswer })
    
    return JsonResponse({ "quiz": quizs[quizId] }) '''