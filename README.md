
# BookMenagerDjango API

BookMenager é uma API RESTful simples desenvolvida com Django, sem o uso do Django Rest Framework (DRF). Esta API permite criar, listar, atualizar e deletar livros.

## Funcionalidades

- **adicionar um novo livro** (`POST /adicionar_livro/`)
- **Listar todas os livros** (`GET /listar_livros/`)
- **Obter um livro por ID** (`GET /livro/<int:id>/`)
- **Atualizar uma tarefa** (`PUT /atualizar_livro/<int:id>/`)
- **Deletar uma tarefa** (`DELETE /deletar_livro/<int:id>/`)

## Model

O projeto utiliza o seguinte modelo `Book`:

```python
from django.db import models

class Book(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()

```

## Views

### 1. Criar um novo livro

```python
from django.shortcuts import render
from app.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json

@@csrf_exempt
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

```

### 2. Listar todas os livros

```python
@csrf_exempt
@require_http_methods(["GET"])
def listar_livros(request):
    if request.method == "GET":
        try:
            livros = Book.objects.all().values()
            return JsonResponse(list(livros),safe=False)
        except Book.DoesNotExist:
            return JsonResponse({"message":"Error Não foi possivel listar os livros"},status=404)

```

### 3. Buscar livro pelo id 

```python
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
            return JsonResponse({"message":"Error Não foi Encontrar o livro"},status=404)

```

### 4. Atualizar livro

```python

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

```

### 5. Deletar livro

```python
@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_livro(request,id):
    try:
        livro = Book.objects.get(id=id)
        livro.delete()
        return JsonResponse({"message":"Livro deletado com sucesso"})
    except Book.DoesNotExist:
        return JsonResponse({"message":"erro não foi possivel deletar este livro ,livro não encontrado"})


```

## Endpoints

### Adicionar Livro

- **URL**: `/adicionar_livro/`
- **Método**: `POST`
- **Body**:

```json
{
  "titulo": "titulo do meu livro",
  "autor": "autor do meu livro",
  "data_publicacao": "yyyy-mm-dd",
  "numero_paginas": "xx"
}
```

- **Resposta**:

```json
{
  "id": 1,
  "message": "Livro adicionada com sucesso"
}
```

### Listar todas as tarefas

- **URL**: `/listar_livro/`
- **Método**: `GET`
- **Resposta**:

```json
[
    {
    "id":0,
    "titulo": "titulo do meu livro",
    "autor": "autor do meu livro",
    "data_publicacao": "yyyy-mm-dd",
    "numero_paginas": "xx"
    },
    {
    "id":0,
    "titulo": "titulo do meu livro",
    "autor": "autor do meu livro",
    "data_publicacao": "yyyy-mm-dd",
    "numero_paginas": "xx"
    }
]
```

### Obter um livro pelo id 

- **URL**: `/livro/<int:id>/`
- **Método**: `GET`
- **Resposta**:

```json
{
    "id":x,
    "titulo": "titulo do meu livro",
    "autor": "autor do meu livro",
    "data_publicacao": "yyyy-mm-dd",
    "numero_paginas": "xx"
    }
```

### Atualizar uma tarefa

- **URL**: `/atualizar_livro/<int:id>/`
- **Método**: `PUT`
- **Body**:

```json
{
    "titulo": "Novo titulo do meu livro",
    "autor": "Novo autor do meu livro",
    "data_publicacao": "yyyy-mm-dd",
    "numero_paginas": "xx"
    }
```

- **Resposta**:

```json
{
  "message": "Livro atualizado com sucesso"
}
```

### Deletar uma tarefa

- **URL**: `/deletar_livro/<int:id>/`
- **Método**: `DELETE`
- **Resposta**:

```json
{
  "message": "Livro deletado com sucesso"
}
```

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/GabrielSouto19/BookMenager_DjangoAPI.git
```
# ATENÇÃO PARA CRIAÇÃO DOS AMBIENTES VIRTUAIS, SIGA O PASSO DE UM OU OUTRO !
2 Crie um ambiente virtual (WINDOWS):

```bash
python -m venv .venv
.venv\Scripts\activate
```

Crie um ambiente virtual (LINUX):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Prepare as migrações:

```bash
python manage.py makemigrations
```
5. Execute as migrações:

```bash
python manage.py migrate
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

5. Acesse a API em `http://localhost:8000/`.

## Observações

- Esta API utiliza views simples do Django e **não** utiliza Django Rest Framework (DRF).
- A proteção CSRF foi desativada com o decorador `@csrf_exempt` para simplificar o uso de métodos `POST`, `PUT` e `DELETE`. Em produção, considere habilitar a proteção CSRF para segurança.
- Para facilitar o processo de testes , recomendo usar a ferramenta postman
