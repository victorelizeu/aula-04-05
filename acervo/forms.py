from django import forms
from .models import Livro


class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["nome", "autor", "descricao", "categorias", "tipo"]

    def clean(self):

        nome = self.cleaned_data.get("nome", "")

        if len(nome) < 2:
            raise forms.ValidationError(f"No! {len(nome)}")
        return nome