from django import forms
from .models import Curso

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
