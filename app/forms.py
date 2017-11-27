from django import forms
from app.models import *
from siteFaculdadev3.settings import *

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"

class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()
    
class QuestaoForm(forms.ModelForm):

    class Meta:
        model = Questao
        exclude = ["curso"]
