"""
Django settings for django_get_started project.
"""


from os import path
import os


#path = "D:\\home\\data\\mysql\\MYSQLCONNSTR_localdb.txt"
pathMysqlConfig = "D:\home\data\mysql\MYSQLCONNSTR_localdb.txt"
mysqlconnopen = open(pathMysqlConfig,'r')
mysqlconnstr = mysqlconnopen.read()

#mysqlconnstr = os.environ['MYSQLCONNSTR_localdb.txt']
mysqlconnlst = mysqlconnstr.split(';')
mysqlconndict = dict(s.split('=',1) for s in mysqlconnlst)

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zne*e2op%jdw&=z4^3p$l@!@$l+15f)w@c3-w-zd137-n8ej0$2'

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'django_get_started.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_get_started.wsgi.application'

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'localdb',
        'USER': 'azure',
        'PASSWORD': '6#vWHD_$',
        'HOST': 127.0.0.1,
        'PORT': '50474',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': mysqlconndict['Database'],
        'USER': mysqlconndict['User Id'],
        'PASSWORD': mysqlconndict['Password'],
        'HOST': mysqlconndict['Data Source'].split(':')[0],
        'PORT': mysqlconndict['Data Source'].split(':')[1],
    }
}

'''
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,"db.slqlite3"),
    }
}
'''

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
