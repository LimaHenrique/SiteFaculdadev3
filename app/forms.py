from django import forms
from app.models import *
from django_get_started.settings import *

class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome", required=True )
    telefone = forms.NumberInput()
    ra = forms.NumberInput()
    assunto = forms.CharField(label="assunto", required=True)
    mensagem = forms.CharField(label="mensagem", required="true")
    
class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = "__all__"
