from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Opere, Categorie
from .models import Risposte, Domande

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
    # --- CODICE FUNZIONANTE ---
    # invenzioni = Opere.objects.all()
    # opt = []
    # for invenzione in invenzioni:
    #     opt.append(invenzione.titolo.lower())
    # return render(request, "invenzioni.html", {"invenzioni": opt})

    # --- DATI FUFFA ---
    invenzioni = ["macchina elettrica rotante", "trasformatore a corrente alternata", "radio a induzione"]
    return render(request, "invenzioni.html", {"invenzioni": invenzioni})


def details(request):
    # --- VERSIONE FUNZIONANTE ---
    # invenzioni = Opere.objects.all()
    # opt = [invenzione.titolo.lower() for invenzione in invenzioni]

    # selected = request.POST.get("invenzione").lower()
    # opera_s = Opere.objects.filter(titolo__iexact=selected).first()

    # if not opera_s:
    #     return render(request, "details.html", {
    #         "errore": "Invenzione non trovata",
    #         "invenzioni": opt
    #     })

    # desc = opera_s.descrizione
    # data = opera_s.data
    # titolo = opera_s.titolo
    # categoria = opera_s.id_categoria.nome  
    # autori = opera_s.autori_set.all()
    # immagini = opera_s.immagini_set.all()

    # return render(request, "details.html", {
    #     "invenzioni": opt,
    #     "invenzione": titolo,
    #     "descrizione": desc,
    #     "data": data,
    #     "categoria": categoria,
    #     "autori": autori,
    #     "immagini": immagini
    # })

    # --- DATI FUFFA ---
    invenzioni = ["macchina elettrica rotante", "trasformatore a corrente alternata", "radio a induzione"]
    selected = request.POST.get("invenzione", "").lower()

    dati_finti = {
        "macchina elettrica rotante": {
            "descrizione": "Dispositivo che converte energia elettrica in meccanica.",
            "data": "1831",
            "categoria": "Scienza e Tecnologia",
            "autori": [{"nome": "Alessandro", "cognome": "Volta"}],
            "immagini": [],
        },
        "trasformatore a corrente alternata": {
            "descrizione": "Permette la trasmissione dell'elettricità su lunghe distanze.",
            "data": "1885",
            "categoria": "Ingegneria",
            "autori": [{"nome": "Nikola", "cognome": "Tesla"}],
            "immagini": [],
        },
        "radio a induzione": {
            "descrizione": "Prototipo per la trasmissione senza fili.",
            "data": "1893",
            "categoria": "Comunicazioni",
            "autori": [{"nome": "Guglielmo", "cognome": "Marconi"}],
            "immagini": [],
        },
    }

    if selected not in dati_finti:
        return render(request, "details.html", {
            "errore": "Invenzione non trovata",
            "invenzioni": invenzioni
        })

    info = dati_finti[selected]

    return render(request, "details.html", {
        "invenzioni": invenzioni,
        "invenzione": selected,
        "descrizione": info["descrizione"],
        "data": info["data"],
        "categoria": info["categoria"],
        "autori": info["autori"],
        "immagini": info["immagini"]
    })



def gamification(request):
    return render(request, "gamification.html")

def game(request):
    return render(request, "game.html")

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