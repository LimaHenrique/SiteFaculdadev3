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
    form = Contato()
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

def questao_form(request,turma=None,questao_id=None):
    if request.POST:
        form = QuestaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/restrito.html")
    else: 
        form = QuestaoForm()
    context = { 
        "form" : form,
        }
    return render(request, "questao_form.html", context)    
