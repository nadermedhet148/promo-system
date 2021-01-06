

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .UserServices import UsersService
from .Repositories.AdministratorUserRepository import AdministratorUserRepository
from .Repositories.NormalUserRepository import NormalUserRepository
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

login_params = openapi.Parameter('user_name', openapi.IN_BODY, description="the User user name", type=openapi.TYPE_STRING)


usersService = UsersService(AdministratorUserRepository() ,  NormalUserRepository())

@swagger_auto_schema(methods=['post'],
                        operation_description="this is end point for administrator user login" ,
                        request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['user_name'],
                             properties={
                                 'user_name': openapi.Schema(type=openapi.TYPE_STRING)
                             },
                         ),
                        responses={
                             200 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'user_name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'token': openapi.Schema(type=openapi.TYPE_STRING),
                                    'id' : openapi.Schema(type=openapi.TYPE_INTEGER)
                                },
                             ),
                             400 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'error': openapi.Schema(type=openapi.TYPE_STRING )
                                }),
                            }
                         )
@api_view(['POST'])
@permission_classes([AllowAny])
def administrator_user_login(request):
    response = usersService.administrator_user_login(request.data.get("user_name"))

    if(response.get('error')):
        return Response(response , status=400)

    return Response(response , status=200)


@swagger_auto_schema(methods=['post'],
                        operation_description="this is end point for administrator user login" ,
                        request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['user_name'],
                             properties={
                                 'user_name': openapi.Schema(type=openapi.TYPE_STRING)
                             },
                         ),
                        responses={
                             200 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'user_name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'token': openapi.Schema(type=openapi.TYPE_STRING),
                                    'id' : openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "mobile_number" : openapi.Schema(type=openapi.TYPE_STRING),
                                },
                             ),
                             400 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'error': openapi.Schema(type=openapi.TYPE_STRING )
                                }),
                            }
                         )
@api_view(['POST'])
@permission_classes([AllowAny])
def normal_user_login(request):
    response = usersService.normal_user_login(request.data.get("user_name"))

    if(response.get('error')):
        return Response(response , status=400)

    return Response(response , status=200)



