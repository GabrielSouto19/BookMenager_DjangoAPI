from django.shortcuts import render
from app.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def listar_livros(request):
    if request.method == "GET":
        try:
            livros = Book.objects.all().values()
            return JsonResponse(list(livros),safe=False)
        except Book.DoesNotExist:
            return JsonResponse({"message":"Error Não foi possivel listar os livros"},status=404)


@csrf_exempt
def adicionar_livro(request):
    if request.method == "POST":
        #lendo o corpo da requisição do json
        dados = json.loads(request.body)
        livro = Book.objects.create(
            titulo=dados.get("titulo"),
            autor=dados.get("autor"),
            data_publicacao=dados.get("data_publicacao"),
            numero_paginas=dados.get("numero_paginas")
        )
        return JsonResponse({"message":"Livro adicionado com secesso"})





@csrf_exempt
def atualizar_livro(request):
    pass


@csrf_exempt
def deletar_livro(request):
    pass

