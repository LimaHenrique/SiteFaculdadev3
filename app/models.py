from django.test import TestCase
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
      #password = models.CharField(max_length=100)
      perfil = models.CharField(max_length=1, default='C')
      ativo = models.BooleanField(default=True)

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

      def __str__(self):
            return self.nome
class Curso(models.Model):
      
      sigla = models.CharField(max_length=5)
      nome = models.CharField(max_length=200)
      tipo = models.CharField(max_length=50,blank=True)
      carga_horaria = models.IntegerField(default=1000)
      ativo = models.BooleanField(default=True)
      descricao = models.TextField(blank=True)
   
      def __str__(self):
            return self.nome

class Disciplina(models.Model):
      nome = models.CharField(max_length=200)
      carga_horaria = models.IntegerField
      conteudo = models.TextField(max_length=1000)

      def __str__(self):
            return self.nome

class CurDis(models.Model):
      curso = models.ForeignKey(

        Curso

      )
      disciplina = models.ForeignKey(

        Disciplina

      )            

class Aluno(Usuario):
      curso = models.ForeignKey(

        Curso

      )

class Professor(Usuario):
      apelido = models.CharField(max_length=30)
      disciplina = models.ForeignKey(
            Disciplina
      )

class Turma(models.Model):
      turma = models.CharField(max_length=240) 
      limite = models.IntegerField(default=40)

class TPA(models.Model):
      turma = models.ForeignKey(

            Turma
      )
      professor = models.ForeignKey(

            Professor
      )    
      curso = models.ForeignKey(
            Curso
      )
      disciplina = models.ForeignKey(
            Disciplina
      )