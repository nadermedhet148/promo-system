
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Users.Repositories.NormalUserRepository import NormalUserRepository
from Promo.Repositories.PromoRepository import PromoRepository 
from Promo.PromoService.PromoService import PromoService
from django.utils.dateparse import parse_date
from .serializers import PromoSerializer


promoService = PromoService(PromoRepository(),NormalUserRepository())

promoSchema = {
'promoType' :openapi.Schema(type=openapi.TYPE_STRING), 
'startTime' :openapi.Schema(type=openapi.TYPE_STRING), 
'endTime' :openapi.Schema(type=openapi.TYPE_STRING), 
'promoAmount' :openapi.Schema(type=openapi.TYPE_NUMBER), 
'isActive' :openapi.Schema(type=openapi.TYPE_BOOLEAN), 
'description' :openapi.Schema(type=openapi.TYPE_STRING), 
'normalUserId' :openapi.Schema(type=openapi.TYPE_INTEGER), 
'promoCode' : openapi.Schema(type=openapi.TYPE_INTEGER),
'creationTime' : openapi.Schema(type=openapi.TYPE_STRING),
'normalUser' : openapi.Schema(type=openapi.TYPE_OBJECT , properties={
    "id":           openapi.Schema(type=openapi.TYPE_INTEGER),
    "name":         openapi.Schema(type=openapi.TYPE_STRING),
    "username":     openapi.Schema(type=openapi.TYPE_STRING),
    "address":      openapi.Schema(type=openapi.TYPE_STRING),
    "mobileNumber": openapi.Schema(type=openapi.TYPE_STRING),
})
}

@swagger_auto_schema(methods=['post'],
                        operation_description="this is end point for administrator user login" ,
                        request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=[ 'promo_type','start_time','end_time','promo_amount','description','normal_user_id'],
                             properties={
                                    'promoType' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'startTime' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'endTime' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'promoAmount' :openapi.Schema(type=openapi.TYPE_NUMBER), 
                                    'isActive' :openapi.Schema(type=openapi.TYPE_BOOLEAN), 
                                    'description' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'normalUserId' :openapi.Schema(type=openapi.TYPE_INTEGER),                              },
                         ),
                        responses={
                             200 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties=promoSchema,
                             ),
                             400 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'error': openapi.Schema(type=openapi.TYPE_STRING )
                                }),
                            }
                         )
@swagger_auto_schema(methods=['get'],
                        operation_description="this is end point get allowed promos for logged in user" ,
                        responses={
                             200 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties=promoSchema,
                             ),
                             400 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'error': openapi.Schema(type=openapi.TYPE_STRING )
                                }),
                            }
                         )
@api_view(['POST' , 'GET'])
@permission_classes([IsAuthenticated])
def mange_promo(request):
    if request.method == "POST":
        response = promoService.create_promo(
            promoType =     request.data.get('promoType') ,
            startTime =     request.data.get('startTime') ,
            endTime =       request.data.get('endTime') ,
            promoAmount =   request.data.get('promoAmount') ,
            isActive =      request.data.get('isActive') ,
            description =   request.data.get('description') ,
            normalUserId =  request.data.get('normalUserId')  , 
            creatorType =   request.user.user_type 
        )
        if(response.get('error')):
            return Response(response , status=400)

        return Response(PromoSerializer(instance=response.get('data')).data , status=200)
    if request.method == 'GET' :
        userType = request.user.user_type
        if userType == 'administrator_user':
            response = promoService.get_promos()

        if(response.get('error')):
            return Response(response , status=400)
        promos = PromoSerializer(response.get('data') , many = True)
        return Response(promos.data , status=200)

@swagger_auto_schema(methods=['PUT'],
                        operation_description="this is end point for edit promo" ,
                        request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=[ 'start_time','end_time','promo_amount'],
                             properties={
                                    'startTime' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'endTime' :openapi.Schema(type=openapi.TYPE_STRING), 
                                    'promoAmount' :openapi.Schema(type=openapi.TYPE_NUMBER), 
                                    'isActive' :openapi.Schema(type=openapi.TYPE_BOOLEAN), 
                                    'description' :openapi.Schema(type=openapi.TYPE_STRING), 
                             }
                         ),
                        responses={
                             200 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties=promoSchema,
                             ),
                             400 : openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'error': openapi.Schema(type=openapi.TYPE_STRING )
                                }),
                            }
                         )
@api_view(['Put'])
@permission_classes([IsAuthenticated])
def modify_promo(request,pk):
    response = promoService.modify_promo(
        startTime =     request.data.get('startTime') ,
        endTime =       request.data.get('endTime') ,
        promoAmount =   request.data.get('promoAmount') ,
        description =   request.data.get('description') ,
        isActive =      request.data.get('isActive') ,
        editorType=   request.user.user_type ,
        promoId =       pk,
    )
    if(response.get('error')):
        return Response(response , status=400)

    return Response(PromoSerializer(instance=response.get('data')).data , status=200)





