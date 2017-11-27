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
    cursos = Curso.objects.all()
    for curso in cursos:
        curso.questoes = Questao.objects.filter(curso=curso)
    contexto = {
        "Cursos": cursos
    }
    return render(request, "restrito.html", contexto)


def questao_form(request,sigla=None,questao_id=None):
    curso = Curso.objects.get(sigla=sigla)
    if request.POST:
        questao = Questao(curso=curso)
        form = QuestaoForm(request.POST, request.FILES,instance=questao)
        if form.is_valid():
            form.save()
            return redirect("/restrito")
    else: 
        if questao_id:
            questao = Questao.objects.get(id=questao_id)    
        else:
            questao = Questao()
        form = QuestaoForm(instance=questao)
    context = { 
        "form" : form,
        "curso" : Curso 
        }
    return render(request, "questao_form.html", context)        
