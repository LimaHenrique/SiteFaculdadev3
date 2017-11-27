from django import forms
from app.models import *
#from django.app.mail import send_mail
from django_get_started.settings import *

class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome", required=True )
    email = forms.EmailField(label="email")
    telefone = forms.NumberInput()
    ra = forms.NumberInput()
    assunto = forms.CharField(label="assunto", required=True)
    mensagem = forms.CharField(label="mensagem", required="true")
    def mandar_email(self, assunto, mensagem, email_enviar):
        print("Agora deu certo.")
        emailOrigem = EMAIL_HOST_USER
        emailDestino = [email_enviar]
        send_mail(assunto, mensagem, emailOrigem, emailDestino, fail_silently=True)
        
class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        exclude = ["turma"]
