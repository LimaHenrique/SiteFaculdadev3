from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm,QuestaoForm
from app.models import *

def index(request):
    context = { "User" : Aluno.objects.all() }
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

def cursos(request):
    form = ContatoForm()
    context = { "cursos.html" : form }
    return render(request, "cursos.html" , context)    
    
def inscricao(request):
    form = ContatoForm()
    context = {"inscricao.html" : form }
    return render(request, "inscricao.html" , context)

def logado(request):
    form = ContatoForm()
    context = {"inscricao.html" : form }
    return render(request, "logado.html" , context)      

def disciplinas(request):
    form = ContatoForm()
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


