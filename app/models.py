from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
      sigla = models.CharField('sigla', primary_key=True, max_length=5)
      nome = models.CharField('nome', unique=True, max_length=50)
      def __str__(self):
            return self.nome
      class Meta:
            db_table = 'Curso'               
class GradeCurricular(models.Model):
      sigla = models.CharField(to='Curso', max_length=5, db_column="sigla_curso", primary_key=True, foreign_key=True, null=False, blank=False, related_name="sigla_curso") 
      ano = models.SmallIntegerField('ano', null=False, primary_key=True)
      semestre = models.CharField('semestre', max_length=1,null=False, primary_key=True)
      def __str__(self):
            return self.semestre
      class Meta:
            db_table = 'GradeCurricular'
class Periodo(models.Model):
      sigla = models.CharField(to='Curso', max_lenght=5, db_column="sigla_curso", primary_key=True, foreign_key=True, null=False, blank=False, related_name="sigla_curso") 
      ano = models.SmallIntegerField(to='GradeCurricular', db_column="ano", primary_key=True, foreign_key=True, null=False, related_name="ano_grade")
      semestre = models.ForeignKey(to='GradeCurricular', max_length=1, primary_key=True, foreign_key=True, db_column="semestre", null=False, related_name="semestre_grade")
      numero = models.TinyIntegerField('numero', max_length=1, null=False, related_name="numero_periodo") 
      def __str__(self):
            return self.__all__
      class Meta:
            db_table = 'Periodo'
class Disciplina(models.Model):
      nome = models.CharField('nome', max_length=240,primary_key=True)
      carga_horaria = models.TinyIntegerField('carga_horaria', null=False)
      teoria = models.DecimalField('teoria', max_digits=3, decimal_places=2)
      pratica = models.DecimalFieldmodels.DecimalField('pratica', max_digits=3, decimal_places=2)
      ementa = models.TextField
      competencias = models.TextField
      habilidades = models.TextField
      conteudo = models.TextField
      bibliografia_basica = models.TextField
      bibliografia_complementar = models.TextField
      def __str__(self):
                return self.__all__
      class Meta:
            db_table = 'Disciplina'
class PeriodoDisciplina(models.Model):
      sigla = models.CharField(to='Curso', max_length=5, db_column="sigla_curso", null=False, primary_key=True, foreign_key=True, blank=False, related_name="sigla_curso")
      ano = models.SmallIntegerField(to='GradeCurricular', db_column="ano", primary_key=True, foreign_key=True, null=False, related_name="ano_grade")
      semestre = models.ForeignKey(to='GradeCurricular', max_length=1, db_column="semestre", primary_key=True, foreign_key=True, null=False, related_name="semestre_grade")
      numero = models.TinyIntegerField(to='GradeCurricular', db_column="semestre", primary_key=True, foreign_key=True, null=False, blank=False,related_name="numero_periodo")
      nome = models.CharField(to='Disciplina', db_column="nome", max_length=240, primary_key=True, foreign_key=True, null=False, blank=False)
class DisciplinaOfertada(models.Model):
      nome = models.CharField(to='Disciplina', max_length=240, db_column="nome", null=False, blank=False)
      ano = models.SmallIntegerField('disciplina_ofertada_ano', null=False)
      semestre = models.CharField('disciplina_ofertada_semestre', max_length=1)
class Aluno(Usuario):
      ra = models.TinyIntegerField('ra', primary_key=True)
      nome = models.CharField('nome', max_length=120)
      email = models.CharField('email', max_length=80)
      celular = models.CharField('celular', max_length=11)
      sigla = models.CharField('sigla_curso', max_length=2)
      list_display = ('nome','ra')
      class Meta:
            db_table = 'Aluno'
class Professor(Usuario):
      ra = models.TinyIntegerField('ra', primary_key=True)
      apelido = models.CharField(unique=True,max_length=30)
      nome = models.CharField('nome', max_length=120)
      email = models.CharField('email', max_length=80)
      celular = models.CharField('celular', max_length=11)
      class Meta:
            db_table = 'Professor'
class Turma(models.Model):
      nome = models.CharField(to='Disciplina', db_column="nome", primary_key=True, foreign_key=True, null=False, blank=False)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column="disciplina_ofertada_ano",  primary_key=True, foreign_key=True, null=False, blank=False, related_name="ano_oferta_disciplina")
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column="disciplina_ofertada_semestre",  primary_key=True, foreign_key=True, null=False, blank=False, related_name="semestre_oferta_disciplina")
      id = models.CharField('id', max_length=1, primary_key=True)
      turno = models.CharField('turno', max_length=15)
      ra = models.TinyIntegerField(to='Professor', foreign_key=True, db_column="ra", null=False, blank=False)
class Matricula(models.Model):
      ra = models.TinyIntegerField(to='Aluno', db_column='ra', foreign_key=True, primary_key=True)
      nome = models.CharField(to='Disciplina', max_length=240, db_column='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='Aluno', db_column='ra', foreign_key=True, primary_key=True)
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(to='Turma', max_length=1, db_column='id', foreign_key=True, primary_key=True)
class CursoTurma(models.Model):
      sigla = models.CharField(to='Curso', max_length=5, db_colum='sigla_curso', foreign_key=True, primary_key=True)
      nome = models.CharField(to='Disciplina', max_length=240, db_colum='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column='disciplina_ofertada_ano', foreign_key=True, primary_key=True)
      smestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_colum='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(id='Turma', max_length=1, db_colum='id', foreign_key=True, primary_key=True)    
class Questao(models.Model):
      nome = models.CharField(to='Disciplina', max_length=240, db_colum='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column='disciplina_ofertada_ano', foreign_key=True, primary_key=True)
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(to='Turma', max_length=1, db_column='id', foreign_key=True, primary_key=True)
      numero = models.TinyIntegerField(primary_key=True)
      data_limite_entrega = models.DateField(auto_now_add=False)
      descricao = models.TextField
      data = models.DateField(auto_now_add=False)
class ArquivosQuestao(models.Model):
      nome = models.CharField(to='Disciplina', max_length=240, db_column='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column='disciplina_ofertada_ano', foreign_key=True, primary_key=True)
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(to='Turma', max_length=1, db_column='id', foreign_key=True, primary_key=True)
      numero = models.IntegerField(to='Questao', foreign_key=True, primary_key=True)
      arquivo = models.CharField('arquivo', max_length=500, primary_key=True)
class Resposta(models.Model):
      nome = models.CharField(to='Disciplina', max_length=240, db_column='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column='disciplina_ofertada_ano', foreign_key=True, primary_key=True)
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(to='Turma', max_length=1, db_column='id', foreign_key=True, primary_key=True)
      numero = models.IntegerField(to='Questao', foreign_key=True, primary_key=True)
      ra = models.TinyIntegerField(to='Aluno', foreign_key=True, db_column="ra", null=False, blank=False, primary_key=True)
      data_avaliacao = models.DateField
      nota = models.DecimalField('nota', max_digits=4, decimal_places=2)
      avaliacao = models.TextField
      descricao = models.TextField
      data_de_envio = models.DateField   
class ArquivosResposta(models.Model):
      nome = models.CharField(to='Disciplina', max_length=240, db_column='nome', foreign_key=True, primary_key=True)
      ano = models.SmallIntegerField(to='DisciplinaOfertada', db_column='disciplina_ofertada_ano', foreign_key=True, primary_key=True)
      semestre = models.CharField(to='DisciplinaOfertada', max_length=1, db_column='disciplina_ofertada_semestre', foreign_key=True, primary_key=True)
      id = models.CharField(to='Turma', max_length=1, db_column='id', foreign_key=True, primary_key=True)
      numero = models.IntegerField(to='Questao', foreign_key=True, primary_key=True)
      ra = models.TinyIntegerField(to='Aluno', foreign_key=True, db_column="ra", null=False, blank=False, primary_key=True)
      arquivo = models.CharField('arquivo', max_length=500, primary_key=True)
