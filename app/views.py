from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        
#"User" : Aluno.objects.all()
        
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
    form = Contato()
    context = {"inscricao.html" : form }
    return render(request, "logado.html" , context)      

def disciplinas(request):
    form = Contato()
    context = {"disciplinas.html" : form }
    return render(request, "disciplinas.html" , context)
