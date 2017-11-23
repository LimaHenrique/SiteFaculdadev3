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
        fields = ('ra', 'nome','apelido')

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
        fields = ('nome','apelido')

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
    list_display = ('ra', 'nome','apelido')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome','password','apelido')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome','apelido')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nome','sigla') 

class DisciplinaAdmin(admin.ModelAdmin):
    
    list_display = ('nome','conteudo','carga_horaria') 

class DisciplinaOfertadaAdmin(admin.ModelAdmin):

    list_display = ('semestre','disciplina') 

class TurmaAdmin(admin.ModelAdmin):
    
    list_display = ('turma','disciplina','professor') 

class QuestaoAdmin(admin.ModelAdmin):
    
    list_display = ('data_limite_entrega','data','turma')     
    
class RespostaAdmin(admin.ModelAdmin):

    list_display = ('data_avaliacao','nota','data_de_envio','questao','aluno') 

class ArquivosQuestaoAdmin(admin.ModelAdmin):
    
    list_display = ('arquivo','questao')     
    
class ArquivosRespostaAdmin(admin.ModelAdmin):

    list_display = ('arquivo','resposta') 

class GradeCurricularAdmin(admin.ModelAdmin):
    
    list_display = ('semestre','curso')   

class CursoTurmaAdmin(admin.ModelAdmin):
    
    list_display = ('curso','turma')   

class MatriculaAdmin(admin.ModelAdmin):
    
    list_display = ('aluno','turma')   

class PeriodoAdmin(admin.ModelAdmin):
    
    list_display = ('gradecurricular')   

class PeriodoDisciplinaAdmin(admin.ModelAdmin):
    
    list_display = ('disciplina','gradecurricular')   
                                
# Register your models here.
admin.site.register(Curso,CursoAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(DisciplinaOfertada,DisciplinaOfertadaAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Questao,QuestaoAdmin)
admin.site.register(Resposta,RespostaAdmin)
admin.site.register(ArquivosQuestao,ArquivosQuestaoAdmin)
admin.site.register(ArquivosResposta,ArquivosRespostaAdmin)
admin.site.register(GradeCurricular,GradeCurricularAdmin)
admin.site.register(CursoTurma,CursoTurmaAdmin)
admin.site.register(Matricula,MatriculaAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(PeriodoDisciplina,PeriodoDisciplinaAdmin)
