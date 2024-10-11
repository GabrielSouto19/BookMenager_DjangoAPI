from django.db import models

class Book(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()



