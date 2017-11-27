from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *
from app.forms import *

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
    form.mandar_email(assunto, mensagem, email)
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

def questao_form(request, turma, questao_id=None):
    turma = Turma.objects.get(turma=turma)

    if questao_id:
        questao = Questao.objects.get(id=questao_id)
    else:
        questao = Questao(turnma=turma)

    if request.POST:
        form = QuestaoForm(request.POST, request.FILES, instance=questao)
        if form.is_valid():
            form.save()
    else:
        form = QuestaoForm(instance=questao)

    contexto = {
        "form":form,
        "turma":turma,
        "questao":Questoes.objects.all()
    }
    return render(request,"questao_form.html",contexto) 
