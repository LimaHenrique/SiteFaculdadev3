from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app.views import *
from django.views.generic import RedirectView
from django.contrib.auth.views import login,logout


urlpatterns = [

    url(r'^$', login,{ 'template_name':'index.html' }),
   # url(r'^index.html', index),
    url(r'^contato.html', login,{ 'template_name':'contato.html' }),
    url(r'^logado.html', login,{ 'template_name':'logado.html' }),
    url(r'^disciplinas.html', login,{ 'template_name':'disciplinas.html' }),
    url(r'^inscricao.html', login,{ 'template_name':'inscricao.html' }),
    url(r'^admin/', admin.site.urls),
    url(r'^cursos.html', login,{ 'template_name':'cursos.html' }),   
    url(r'^eventos.html', login,{ 'template_name':'eventos.html' }),
    url(r'^blog.html', login,{ 'template_name':'blog.html' }),
    url(r'^index.html', login,{ 'template_name':'index.html' }),
    url(r'^sair/', logout , {'next_page': '/index.html'})
    
]