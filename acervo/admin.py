from django.contrib import admin
from .models import Livro, Autor, Categoria, Tipo_Acervo

# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Tipo_Acervo)
