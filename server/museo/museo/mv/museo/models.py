from django.db import models

# Create your models here.
class Utenti (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=50)

class Categorie(models.Model):
    nome = models.CharField(max_length=50)

class Opere (models.Model):
    descrizione = models.TextField()
    data = models.DateField()
    titolo = models.CharField(max_length=50)
    id_categoria = models.ForeignKey(Categorie, on_delete = models.CASCADE)

class Immagini (models.Model):
    img = models.BinaryField()
    descrizione = models.TextField()
    id_opera = models.ForeignKey(Opere, on_delete = models.CASCADE)

class Autori (models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateField()
    data_morte = models.DateField()
    vita = models.TextField()
    opere = models.ManyToManyField(Opere)

class Quiz (models.Model):
    categoria = models.CharField(max_length=50)

class Domande (models.Model):
    body = models.TextField()
    url_pagina = models.URLField()
    id_quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)

    def __str__(self):
        return self.body

class Risposte (models.Model):
    body = models.TextField()
    isRisposta = models.BooleanField(default=False)
    id_domanda = models.ForeignKey(Domande, on_delete = models.CASCADE)

    def __str__(self):
        return self.body
    
class Partite (models.Model):
    punteggio = models.IntegerField()
    quiz = models.ManyToManyField(Quiz)
    terminato = models.BooleanField(default=False)
    id_utente = models.ForeignKey(Utenti, on_delete= models.CASCADE)
