import os

PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
SECRET_KEY = 'ABCD4C7Q4rfThde4rNtDuEBoLuXeRtg'
ROOT_URLCONF = 'djangoproject.urls'

TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public')

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, 'static')]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

DRF_CHAOS_ENABLED = True

MIDDLEWARE_CLASSES = [
    # 'drf_chaos.middleware.ChaosMiddleware'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_chaos',
]
