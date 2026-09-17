from . import views
from django.urls import path

urlpatterns = [
    path("", views.lista_livros, name="lista"),
    path("novo/", views.novo_livro, name="novo")
]
