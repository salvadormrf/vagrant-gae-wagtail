import os
import sys
import importlib

from django.core.exceptions import ImproperlyConfigured


ALLOWED_ENVS = (
    # Local development
    'local',
    # Appengine with environment variables
    'gae',
)

env = os.environ.get('DJANGO_ENV', 'local').lower()


if not env:
    raise ImproperlyConfigured("You must define 'DJANGO_ENV' on your environment variables")
if env not in ALLOWED_ENVS:
    raise ImproperlyConfigured("Env '%s' is not allowed" % env)

# Bring vars from env-specific settings file into scope
curr_module = sys.modules[__name__]
env_settings = importlib.import_module('.%s' % env, package=__package__)

for var, value in vars(env_settings).iteritems():
    setattr(curr_module, var, value)
