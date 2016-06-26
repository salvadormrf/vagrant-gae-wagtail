"""
Namespacing:

Applies to datastore, memcache and task queues
See: https://developers.google.com/appengine/docs/python/multitenancy/multitenancy#Setting_the_Current_Namespace
"""
import os
import re

from manage import add_extra_paths
add_extra_paths()

# Here we will be an unique namespace per version
namespace = os.environ.get('GAE_NAMESPACE', 'local')


def namespace_manager_default_namespace_for_request():
    return namespace
