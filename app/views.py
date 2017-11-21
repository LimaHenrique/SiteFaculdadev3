from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def contato(request):
    return render(request, "contato.html")
def cursos(request):
    return render(request, "cursos.html")
def eventos(request):
    return render(request, "eventos.html")
def inscricao(request):
    return render(request, "inscricao.html")
def blog(request):
    return render(request, "blog.html")
