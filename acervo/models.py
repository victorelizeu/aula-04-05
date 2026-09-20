from django.db import models

# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    CATEGORIAS_CHOICES = [
        ("000", "000 – Generalidades e Informação"),
        ("100", "100 – Filosofia e Psicologia"),
        ("200", "200 – Religião e Teologia"),
        ("300", "300 – Ciências Sociais e Direito"),
        ("400", "400 – Linguística e Idiomas"),
        ("500", "500 – Ciências Puras (Exatas e Naturais)"),
        ("600", "600 – Ciências Aplicadas (Tecnologia)"),
        ("700", "700 – Artes e Recreação"),
        ("800", "800 – Literatura"),
        ("900", "900 – História e Geografia"),
    ]

    TIPO_CHOICES = [("digital", "Digital"), ("fisico", "Físico")]

    nome = models.CharField(max_length=300)
    descricao = models.TextField(blank=False)

    autor = models.ForeignKey(Autor, related_name="livro", on_delete=models.CASCADE)
    categorias = models.CharField(max_length=10, choices=CATEGORIAS_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome
