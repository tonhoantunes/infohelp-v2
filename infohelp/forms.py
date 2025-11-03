from django import forms
from .models import Curso, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'titulo',
            'descricao',
            'categoria',
            'dificuldade',
            'imagem',
            'link_video',
            'carga_horaria',
            'ativo'
        ]
