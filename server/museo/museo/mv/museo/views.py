from django.shortcuts import render


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
    opt = ["Pila", "Metano",]
    return render(request, "invenzioni.html", {"invenzioni": opt})


def details(request):
    opt = ["Pila", "Metano", ]
    selected = request.POST.get("invenzione").lower()
    return render(request, f"{selected}.html", {"invenzioni": opt})
