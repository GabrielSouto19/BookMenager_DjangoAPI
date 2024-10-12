from django.contrib import admin
from django.urls import path
from app.views import listar_livros,adicionar_livro,atualizar_livro,deletar_livro,obter_livro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_livros', listar_livros,name="listar_livros"),
    path('livro/<int:id>', obter_livro,name="obter_livro"),
    path('adicionar_livro', adicionar_livro,name="adicionar_livro"),
    path('atualizar_livro/<int:id>', atualizar_livro,name="atualizar_livro"),
    path('deletar_livro/<int:id>', deletar_livro,name="deletar_livro"),
]
