from django.shortcuts import render
from django.http import HttpResponse
from .models import Opere

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
        opt.append(invenzione.nome.lower())
    
    return render(request, "invenzioni.html", {"invenzioni": opt})


def details(request):
    invenzioni = Opere.objects.all()
    opt = []
    for invenzione in invenzioni:
        opt.append(invenzione.nome.lower())
   
    selected = request.POST.get("invenzione").lower()
    return render(request, f"{selected}.html", {"invenzioni": opt})

def gamification(request):
    return render(request, "gamification.html")

def quiz(request):
    return HttpResponse({ "chiave":"valore"})