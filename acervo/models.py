from django.db import models

# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Tipo_Acervo(models.Model):
    estado = (
        ("digital", "Digital"),
        ("fisico", "Físico")
    )

    tipo = models.CharField(max_length=150, blank=False,
                            choices=estado, null=False)

    def __str__(self):
        return self.tipo


class Categoria(models.Model):
    estado = [
        ("000 –", "Generalidades e Informação: Obras gerais, enciclopédias, jornais e biblioteconomia"),
        ("100 –", "Filosofia e Psicologia: Ética, lógica e investigações sobre a mente humana"),
        ("200 –", "Religião e Teologia: Mitologia, teologia e estudos sobre crenças e religiões"),
        ("300 – ", "Ciências Sociais e Direito: Política, economia, sociologia, educação e leis"),
        ("400 – ", "Linguística e Idiomas: Gramáticas, dicionários e estudos de línguas"),
        ("500 – ", "Ciências Puras (Exatas e Naturais): Matemática, física, química, biologia e astronomia"),
        ("600 – ", "Ciências Aplicadas (Tecnologia): Medicina, engenharia, agricultura e administração"),
        ("700 – ", "Artes e Recreação: Pintura, música, arquitetura, esportes e lazer"),
        ("800 – ", "Literatura: Poesia, romances, contos, crônicas e crítica literária"),
        ("900 – ", "História e Geografia: Biografias, viagens e acontecimentos históricos")
    ]

    categorias = models.CharField(
        max_length=300, choices=estado, blank=False)

    def __str__(self):
        return self.categorias


class Livro(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.TextField(blank=False)

    autor = models.ForeignKey(
        Autor, related_name="livro", on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, related_name="livro")
    tipo = models.ForeignKey(
        Tipo_Acervo, on_delete=models.CASCADE, related_name="livro")

    def __str__(self):
        return self.nome
