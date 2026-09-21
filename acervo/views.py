from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForms
from django.db.models import Q

# Create your views here.


def lista_livros_solo(request):
    livros = Livro.objects.all()

    q = request.GET.get("q", "").strip()

    if q:
        livros = livros.filter(
            Q(nome__icontains=q), Q(tipo__icontains=q), Q(categorias__icontains=q)
        )

    return render(request, "acervo/lista_pesquisa.html", {"lista": livros, "query": q})


def novo_livro(request):
    if request.method == "POST":
        book = LivroForms(request.POST)

        if book.is_valid():
            book.save()

            return redirect("lista")
    else:
        book = LivroForms()

    return render(request, "acervo/form.html", {"novo": book})


def lista_livros(request):
    book = Livro.objects.all()
    return render(request, "acervo/lista.html", {"lista": book})
