"""
Django settings for authors project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import datetime

import django_heroku

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY") or "secret"

APP_SETTINGS = os.getenv("APP_SETTINGS")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #if APP_SETTINGS == "development" else False

ALLOWED_HOSTS = ['*']
# Application definition
CORS_ORIGIN_ALLOW_ALL=True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'corsheaders',
    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    'authors.apps.authentication',
    'authors.apps.core',
    'authors.apps.profiles',
    'authors.apps.articles',
    'authors.apps.friends',
    'authors.apps.likedislike',
    'authors.apps.comments',
    'authors.apps.bookmarks',
    'authors.apps.stats',
    'authors.apps.highlight',
    'authors.apps.reports',
    'authors.apps.favorites',
    'authors.apps.usernotifications',
    
    'notifications'
]

MIDDLEWARE = [
    # 'djdev_panel.middleware.DebugMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware'
]

ROOT_URLCONF = 'authors.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'authors.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'ah-sealteam/media')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
CORS_ORIGIN_WHITELIST = (
    '0.0.0.0:4000',
    'localhost:4000',
)

# Tell Django about the custom `User` model we created. The string
# `authentication.User` tells Django we are referring to the `User` model in
# the `authentication` module. This module is registered above in a setting
# called `INSTALLED_APPS`.
AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'authors.apps.core.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authors.apps.authentication.backends.JWTAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 100
}

DOMAIN = os.getenv("DOMAIN")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user', 'repo'],
        'FIELDS': [
            'email',
            'username'
        ]
        },

    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v3.2',
    },
    'google': {
        'METHOD': 'oauth2',
        'SCOPE': ['email'],
        'FIELDS': [
            'email'
        ]
    }
}

SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
SOCIALACCOUNT_ADAPTER = 'authors.apps.authentication.adapter.SocialAccountAdapter'
REST_USE_JWT = True
ACCOUNT_SIGNUP_FORM_CLASS = 'authors.apps.authentication.forms.CustomUserCreationForm'
SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'USE_SESSION_AUTH': False,
    'DOC_EXPANSION': 'list',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
}

DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
    'SOFT_DELETE':True 
}


REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER":'authors.apps.authentication.serializers.CustomUserDetailsSerializer'
}

django_heroku.settings(locals(), logging=not DEBUG)

locals()['DATABASES']['default'] = dj_database_url.config(engine='django.db.backends.postgresql',
                                                          ssl_require=not DEBUG)

TOKEN_EXPIRE_TIME = datetime.timedelta(seconds=3)
