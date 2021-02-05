import re

import django.contrib.auth.models as authmodels

import apps.core.models as coremodels

def get_realm_from_request(request):
    match = re.match(r'^/realms/(?P<realm>[a-z]+)/', request.path)
    return None if not match else match.group(1)
