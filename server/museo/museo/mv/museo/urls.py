from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("biografia", views.biografia, name="biografia"),
    path("invenzioni", views.invenzioni, name="invenzioni"),
    path("tvolt", views.tvolt, name="tvolt"),
    path("details", views.details, name='details'),
    path("gamification", views.gamification, name='gamification'),
]
