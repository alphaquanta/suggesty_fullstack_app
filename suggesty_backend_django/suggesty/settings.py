"""
Django settings for suggesty project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import sys
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except:
    print("SECRET_KEY not found in environment default key in use. This may cause security problems")
    SECRET_KEY = 'django-insecure-)s*)wx2j#k8yy90q1_k5nsc#cqzc+)otz0go(0puj$lh)qa5zk'


try:
    SPOTIFY_CLIENTID = os.environ['SPOTIFY_CLIENTID']
    SPOTIFY_CLIENTSECRET = os.environ['SPOTIFY_CLIENTSECRET']
    SPOTIFY_API_URL = os.environ['SPOTIFY_API']
except:
    print("Spotify Secrets not found in environment default key in use. This may cause security problems.")
    SPOTIFY_CLIENTID = "47023500e54a405f933b8abf0a90b89e" 
    SPOTIFY_CLIENTSECRET = "4a6c73d77a774dd382988b2b79a96570"
    SPOTIFY_API_URL = "https://api.spotify.com/"


# SECURITY WARNING: don't run with debug turned on in production!
try: 
    DEBUG = os.environ['RuntimeEnv'] == "DEV"
except:
    DEBUG = True #In case value not in the env values, assume it is dev env.

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'apps.tracks'
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'suggesty.urls'

#TEMPLATES = [
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#    {
#        'DIRS': [],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.debug',
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]

WSGI_APPLICATION = 'suggesty.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# Left as enabled to able to run the tests..
if 'test' in sys.argv:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
   }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
