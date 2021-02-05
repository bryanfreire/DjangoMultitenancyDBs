import threading

import django.http as http
import django.contrib.auth.models as authmodels
import rest_framework.authtoken.models as tokenmodels

import apps.core.utils as coreutils


THREAD_LOCAL = threading.local()

def set_db_name(db):
    setattr(THREAD_LOCAL, "DB", db)

def get_db_name():
    return getattr(THREAD_LOCAL, "DB", None)

class RealmsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __respond__(self, msg):
        return http.JsonResponse(
            {
                'detail': msg
            },
            status = 401 # Unauthorized
        )

    def __call__(self, request):
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][6:]
            if tokenmodels.Token.objects.filter(key=token).exists():
                url_realm = coreutils.get_realm_from_request(request)
                user = tokenmodels.Token.objects.get(key=token).user
                if (
                    url_realm and user.realms.filter(name=url_realm) or
                    user.is_superuser
                ):
                    set_db_name(url_realm)
                    response = self.get_response(request)
                else:
                    response = self.__respond__('Invalid token. Not authorized.')
            else:
                response = self.__respond__('Invalid token.')
        else:
            response = self.__respond__('Authorization token not provided')
        return response
