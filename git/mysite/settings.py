"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a6yfdbdndyqmb5f$f0$_gi*jkr(6=cu9l(qjkq0rfdwuif(48%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learn',
    'captcha'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS= (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/')),

)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS =False
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'postmaster@seeksrq.top'
EMAIL_HOST_PASSWORD = 'lsrq.0218'
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(hidden_field)s %(image)s'
# 噪点样式
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',  # 没有样式
                           # 'captcha.helpers.noise_arcs', # 线
                           # 'captcha.helpers.noise_dots', # 点
                           )
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 25)
CAPTCHA_BACKGROUND_COLOR = '#eeeeee'
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 图片中的文字为随机英文字母，如 mdsh
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'    # 图片中的文字为数字表达式，如1+2=</span>

CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
