from django import forms
from app.models import Questao
from django.core.mail import send_mail
from siteFaculdade.settings import *

class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome", required=True )
    email = forms.EmailField(label="email", help_text="Informe um e-mail válido")
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
        fields = "__all__"
