from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.core.mail import send_mail
from django_get_started.settings import *

def index(request):

    context = {
        
        "User" : Aluno.objects.all()
        
    }
    return render(request, "index.html")

def contato(request):
    
    form = ContatoForm(request.POST)
    
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    assunto = request.POST.get('assunto')
    conteudo_mensagem = request.POST.get('mensagem')
    mensagem = "Nome: {}. Telefone: {}. Mensagem: {}".format(nome, telefone, conteudo_mensagem)
    
    emailOrigem = EMAIL_HOST_USER
    emailDestino = [email]
    
    #send_mail(assunto, mensagem, emailOrigem, emailDestino, fail_silently=True)
    send_mail("assunto", "mensagem", "siteimpactav3@hotmail.com", "siteimpactav3@hotmail.com", fail_silently=True)
    
    context = { "contato.html" : form }
    return render(request, "contato.html" , context)

def blog(request):
    form = Contato()    
    context = { "blog.html" : form }
    return render(request, "blog.html" , context)

def eventos(request):
    form = Contato()
    context = { "eventos.html" : form }
    return render(request, "eventos.html" , context)

def cursos(request):
    form = Contato()
    context = { "cursos.html" : form }
    return render(request, "cursos.html" , context)    
    
def inscricao(request):
    form = Contato()
    context = {"inscricao.html" : form }
    return render(request, "inscricao.html" , context)

def logado(request):
    form = ContatoForm()
    context = {"inscricao.html" : form }
    return render(request, "logado.html" , context)  


def disciplinas(request):
    form = Contato()
    context = {"disciplinas.html" : form }
    return render(request, "disciplinas.html" , context)	

def restrito(request):
    context = {
        "turmas" : Turma.objects.all()
    }
    return render(request, "restrito.html", context)

def questao_form(request, numero, arquivosquestao_id=None):
    questao = Questao.objects.get(numero=numero)

    if questao_id:
        arquivosquestao = ArquivosQuestao.objects.get(id=arquivosquestao_id)
    else:
        arquivosquestao = ArquivosQuestao(questao=questao)

    if request.POST:
        form = QuestaoForm(request.POST, request.FILES, instance=arquivosquestao)
        if form.is_valid():
            form.save()
            return redirect("/restrito.html")
    else:
        form = QuestaoForm(instance=arquivosquestao)

    contexto = {
        "form":form,
        "questao":Questao,
       
    }
    return render(request,"questao_form.html",contexto) 
