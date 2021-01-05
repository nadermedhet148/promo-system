

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .UserServices import UsersService
from .models import AdministratorUser , NormalUser

usersService = UsersService(AdministratorUser , NormalUser)

@api_view(['POST'])
@permission_classes([AllowAny])
def administrator_user_login(request):
    response = usersService.administrator_user_login(request.data.get("user_name"))

    if(response.get('error')):
        return Response(response , status=400)

    return Response(response , status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def normal_user_login(request):
    response = usersService.normal_user_login(request.data.get("user_name"))

    if(response.get('error')):
        return Response(response , status=400)

    return Response(response , status=200)



