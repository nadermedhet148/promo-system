import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model


class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            user_data = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')



        return (user_data, None)


