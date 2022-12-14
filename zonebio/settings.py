"""
Django settings for zonebio project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*zczz#c1xms^%syefidafv8!(j!-h-4!e0+i!l=uk%1wj(&16n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'mybiodata.apps.MybiodataConfig',
    'bootstrap4',                   #Cela suffit à utiliser Bootstrap ? (Non)
    'mptt',         #Voir https://django-page-cms.readthedocs.io/en/latest/installation.html#evaluate-quickly-the-application
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #Element ajouté pour utiliser Gerbi
    'django_extensions' # Element ajouté pour télécharger des librairies créées par d'autres (ou par soi-même)
]

#Elément ajouté pour pouvoir utiliser Gerbi
PAGE_DEFAULT_TEMPLATE = 'pages/index.html'

#Gerbi demande beaucoup de choses pour les langages
# Default language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# here is all the languages supported by the CMS
PAGE_LANGUAGES = (
    ('de', gettext_noop('German')),
    ('fr', gettext_noop('Français')),
    ('en', gettext_noop('US English')),
)

# copy PAGE_LANGUAGES
languages = list(PAGE_LANGUAGES)

# redefine the LANGUAGES setting in order to be sure to have the correct request.LANGUAGE_CODE
LANGUAGES = languages

#Elément à ajouter pour utiliser Gerbi
PAGE_USE_SITE_ID = False
SITE_ID = 1

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}  #Trucs ajoutés pour télécharger des bibliothèques personnalisées

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zonebio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.media',   #Il faut ajouter cet élément pour utiliser Gerbi
            ],
        },
    },
]

WSGI_APPLICATION = 'zonebio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#Après avoir ajouté STATICFILES, il faut ajouter
#cette ligne pour que Django puisse utiliser
#le sous-dossier "images" de "static"

MEDIA_URL = '/images/'

#Il faut ajouter la variable STATICFILES_DIRS
#pour que Django puisse localiser les sous-dossiers
#du dossier "static"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
