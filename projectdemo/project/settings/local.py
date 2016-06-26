# Import common settings from base
from .base import *

DEBUG = True

# Allow to run from any domain
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable HTTPS redirection
SECURE_SSL_REDIRECT = False

# Allow sending cookies over HTTP
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

GS_BUCKET_NAME = 'projectdemo-local'

# Develop with mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projectdemo',
        'USER': 'projectdemo',
        'HOST': 'localhost',
        'PORT': '3306',
        'PASSWORD': 'projectdemo',
        'CONN_MAX_AGE': 0,  # number of seconds database connections should persist for
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8',
            'init_command': 'SET '
            'storage_engine=INNODB,'
            'character_set_connection=utf8,'
            'collation_connection=utf8_bin,'
            'SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
        }
    }
}

# Enable development apps
INSTALLED_APPS += (
    'projectapps.dev',
)

"""
# Enable debug toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = '192.168.2.10'

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}
"""

try:
    from local_settings import *
except ImportError:
    pass
