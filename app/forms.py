from django import forms
from app.models import *
from django_get_started.settings import *

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"

class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()
    
class QuestaoForm(forms.Form):

    class Meta:
        model = Questao
        fields = "__all__"
