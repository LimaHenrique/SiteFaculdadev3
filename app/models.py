from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
      use_in_migrations = True
      def _create_user(self, ra, password, **extra_fields):
          if not ra:
              raise ValueError('RA precisa ser preenchido')
          user = self.model(ra=ra, **extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user

      def create_user(self, ra, password=None, **extra_fields):
          return self._create_user(ra, password, **extra_fields)

      def create_superuser(self, ra, password, **extra_fields):
          return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
      nome = models.CharField(max_length=50)
      ra = models.IntegerField(unique=True)
      perfil = models.CharField(max_length=1, default='C')
      ativo = models.BooleanField(default=True)
      email = models.CharField(max_length=80)
      celular = models.CharField(max_length=11)

      USERNAME_FIELD = 'ra'
      REQUIRED_FIELDS = ['nome']

      objects = UsuarioManager()

      @property
      def is_staff(self):
            return self.perfil == 'C'

      def has_perm(self, perm, obj=None):
            return True
      
      def has_module_perms(self, app_label):
            return True
  
      def get_short_name(self):
            return self.nome
      
      def get_full_name(self):
            return self.nome

      def _str_(self):
            return self.nome

class Curso(models.Model):
      sigla = models.CharField(max_length=5)
      nome = models.CharField(unique=True)                  

class GradeCurricular(models.Model):
      ano = models.Field
      semestre = models.CharField(max_length=1)
      curso = models.ForeignKey(

        Curso

      )

class Periodo(models.Model):
      numero = models.TinyintField
      gradecurricular = models.ForeignKey(

        GradeCurricular

      )

class Disciplina(models.Model):
      nome = models.CharField(max_length=240)
      carga_horaria = models.Tinyint
      teoria = models.DecimalField(max_length=3)
      pratica = models.DecimalField(max_length=3)
      ementa = models.TextField
      competencias = models.TextField
      habilidades = models.TextField
      conteudo = models.TextField
      bibliografia_basica = models.TextField
      bibliografia_complementar = models.TextField

class PeriodoDisciplina(models.Model):
      gradecurricular = models.ForeignKey(

        GradeCurricular

      )
      disciplina = models.ForeignKey(

        Disciplina

      )

class DisciplinaOfertada(models.Model):
      ano = models.SmallIntegerField
      semestre = models.CharField(max_length=1)
      disciplina = models.ForeignKey(

        Disciplina

      )

class Aluno(Usuario):
      curso = models.ForeignKey(

        Curso

      )

class Professor(Usuario):
      apelido = models.CharField(unique=True,max_length=30)

class Turma(models.Model):
      turma = models.CharField(max_length=15)
      disciplinaofertada = models.ForeignKey(

        DisciplinaOfertada

      )
      professor = models.ForeignKey(

        Professor

      )

class Matricula(models.Model):
      aluno = models.ForeignKey(

        Aluno

      )
      turma = models.ForeignKey(

        Turma

      )

class CursoTurma(models.Model):
      curso = models.ForeignKey(

        Curso

      )
      turma = models.ForeignKey(

        Turma

      )

class Questao(models.Model):
      numero = models.SmallIntegerField
      data_limite_entrega = models.DateField
      descricao = models.TextField
      data = models.DateField
      turma = models.ForeignKey(

        Turma

      )

class ArquivosQuestao(models.Model):
      numero_questao = models.IntegerField
      arquivo = models.CharField(max_length=500)
      questao = models.ForeignKey(

        Questao

      )

class Resposta(models.Model):
      questao = models.ForeignKey(

        Questao

      )
      aluno = models.ForeignKey(

        Aluno

      )
      data_avaliacao = models.DataField
      nota = models.DecimalField(decimal_places=4,max_digits=2)
      avaliacao = models.TextField
      descricao = models.TextField
      data_de_envio = models.DateField

class ArquivosResposta(models.Model):
      resposta = models.ForeignKey(

        Resposta

      )      
      arquivo = models.CharField(max_length=500)
