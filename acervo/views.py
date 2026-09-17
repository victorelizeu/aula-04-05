from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForms

# Create your views here.


def lista_livros(request):
    book = Livro.objects.all()
    return render(request, "acervo/lista.html", {"lista": book})


def novo_livro(request):
    if request.method == "POST":
        book = LivroForms(request.POST)

        if book.is_valid():
            book.save()

            return redirect("lista")
    else:
        book = LivroForms()

    return render(request, "acervo/form.html", {"novo": book})
