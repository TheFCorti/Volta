from django.shortcuts import render
from django.http import HttpResponse
from .models import Opere, Categorie

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
    return render(request, "game.html")

def quiz(request):
    quizId = request.GET.get('quizId')
    questionId = request.GET.get('questionId')
    answerId = request.GET.get('answerId')
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

    if not quizId:
        return JsonResponse({ "error": {
            "message": "quizId not provided",
        }})
    
    selectedQuiz = quizs[quizId]
    
    if questionId and answerId:
        correctAnswer = selectedQuiz.domande[questionId].risposte[answerId]
        return JsonResponse({ "correctAnswer": True })
    
    return JsonResponse({ "quiz": quizs[quizId] })