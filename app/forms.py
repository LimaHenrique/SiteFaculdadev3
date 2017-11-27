from django import forms
from app.models import *
from django.core.mail import send_mail
from siteFaculdade.settings import *

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
