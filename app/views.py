from django.shortcuts import render
from app.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


@csrf_exempt
@require_http_methods(["GET"])
def listar_livros(request):
    if request.method == "GET":
        try:
            livros = Book.objects.all().values()
            return JsonResponse(list(livros),safe=False)
        except Book.DoesNotExist:
            return JsonResponse({"message":"Error Não foi possivel listar os livros"},status=404)

@csrf_exempt
@require_http_methods(["GET"])
def obter_livro(request,id):
    if request.method == "GET":
        try:
            livros = Book.objects.get(id=id)
            dados = {
                "titulo":livros.titulo,
                "autor":livros.autor,
                "data_publicacao":livros.data_publicacao,
                "numero_paginas":livros.numero_paginas,
            }
            return JsonResponse(dados)
        except Book.DoesNotExist:
            return JsonResponse({"message":"Error Não foi possivel listar os livros"},status=404)




@csrf_exempt
@require_http_methods(["POST"])
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
@require_http_methods(["PUT"])
def atualizar_livro(request,id):
    if request.method == "PUT":
        try:
            livro = Book.objects.get(id=id)
            dados = json.loads(request.body)
            livro.titulo = dados.get("titulo",livro.titulo)
            livro.autor = dados.get("autor",livro.autor)
            livro.data_publicacao = dados.get("data_publicacao",livro.data_publicacao)
            livro.numero_paginas = dados.get("numero_paginas",livro.numero_paginas)
            livro.save()
            return JsonResponse({"message":"livro atualizado com sucesso"})
        
        except Book.DoesNotExist:
            return JsonResponse({"message":"Erros livro não encontrado"})

    return JsonResponse({"message":"erro , não foi possivel atualizar o livro"},status=404)



@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_livro(request,id):
    try:
        livro = Book.objects.get(id=id)
        livro.delete()
        return JsonResponse({"message":"Livro deletado com sucesso"})
    except Book.DoesNotExist:
        return JsonResponse({"message":"erro não foi possivel deletar este livro ,livro não encontrado"})


