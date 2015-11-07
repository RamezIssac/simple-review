# from marmina_farm.settings.base import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.admindocs',
    # 'django.contrib.formtools',

    # 'django_nose',
    # 'reversion',
    'simple_review',
    "test_app",


    # 'tests.admin_views',
    # # 'tests.ra_config',
    # 'django_bootstrap_breadcrumbs',
    # 'sitetree',

    'django.contrib.admin',

]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django'
    },
    'other': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
ROOT_URLCONF = 'tests.urls'

MIDDLEWARE_CLASSES = (
    # 'debug_panel.middleware.DebugPanelMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'reversion.middleware.RevisionMiddleware',

)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, '../static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    # 'compressor.finders.CompressorFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR,'..', 'collected_static')
