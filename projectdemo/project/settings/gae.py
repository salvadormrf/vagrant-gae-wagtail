import os

# Import common settings from base
from .base import *

# Disable debug mode
DEBUG = bool(os.environ.get('APP_DEBUG', False))


# The same as GAE version
GAE_VERSION = os.environ.get('APP_GAE_VERSION', '')

ALLOWED_HOSTS = [
    '{version}-dot-{app_id}.appspot.com'.format(version=GAE_VERSION, app_id='projectdemo-appid'),
    '{version}.{app_id}.appspot.com'.format(version=GAE_VERSION, app_id='projectdemo-appid'),
]

# File storage settings
GS_BUCKET_NAME = os.environ.get('APP_GS_BUCKET_NAME', None)


TEMPLATES[0]['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]


CACHES = {
    'default': {
        'BACKEND': 'gaekit.caches.GAEMemcachedCache',
    }
}


# Database access
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('APP_DATABASE_NAME', ''),
        'USER': os.environ.get('APP_DATABASE_USER', ''),
        'HOST': os.environ.get('APP_DATABASE_HOST', ''),
        'PORT': os.environ.get('APP_DATABASE_PORT', ''),
        'PASSWORD': os.environ.get('APP_DATABASE_PASS', ''),
        'CONN_MAX_AGE': 0,  # Number of seconds database connections should persist for.
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
