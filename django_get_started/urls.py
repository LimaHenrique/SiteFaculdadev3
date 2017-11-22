
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^contato.html', contato),
    url(r'^inscricao.html', inscricao),
    url(r'^index.html', index),
    url(r'^cursos.html', cursos),
    url(r'^eventos.html', eventos),
    url(r'^blog.html', blog)
    
]

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
