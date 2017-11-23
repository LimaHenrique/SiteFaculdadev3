from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin
from django import forms

class NovoAlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ('ra', 'nome','curso','perfil')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        if commit:
            user.save()
        return user

class NovoProfessorForm(forms.ModelForm):
    
    class Meta:
        model = Professor
        fields = ('ra', 'nome','disciplina','apelido')

    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'P'
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'curso')

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'disciplina','apelido')

class AlunoAdmin(UserAdmin):
    
    form =  AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'curso','password')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'curso')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class ProfessorAdmin(UserAdmin):
    
    form =  AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'disciplina','apelido')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'disciplina','password','apelido')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'disciplina','apelido')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class cursoAdmin(admin.ModelAdmin):

    list_display = ('nome','tipo','carga_horaria') 

class DisciplinaAdmin(admin.ModelAdmin):
    
    list_display = ('nome','conteudo','carga_horaria') 

# Register your models here.
admin.site.register(Curso,cursoAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
