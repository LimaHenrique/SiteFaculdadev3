from django import forms

class Contato(forms.Form):
    assunto = forms.CharField(label="Assunto", required = True)
    nome = forms.CharField(label="Nome",required = True )
    email = forms.EmailField(label="E-mail", help_text="Informe um E-mail válido")
    telefone = forms.NumberInput()
    mensagem = forms.CharField(label = "Mensagem" , required = "true")
