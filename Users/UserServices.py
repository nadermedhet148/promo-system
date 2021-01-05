import datetime
import jwt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class UsersService:

    def __init__(self,administratorUserModel,normalUserModel):
        self.administratorUserModel = administratorUserModel
        self.normalUserModel = normalUserModel


    def generate_access_token(self,user_id ,user_type):
        
        access_token_payload = {
            'user_id': user_id,
            'user_type' : user_type,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
            'iat': datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(access_token_payload,
                                settings.SECRET_KEY, algorithm='HS256')
        return access_token

    
    def administrator_user_login(self, username) :
        try:
            administrator_user = self.administratorUserModel.objects.get(username=username)
            return {
                "data" : {
                    "token" : self.generate_access_token(administrator_user.id, 'administrator_user'),
                    "username" : administrator_user.username,
                    "id" : administrator_user.id,
                }
            }
        except ObjectDoesNotExist:
            return {
               "error" : {
                    "message" : 'sorry this user isn\'t exists',
               }  
            }
    def normal_user_login(self, username) :
            try:
                normal_user = self.normalUserModel.objects.get(username=username)
                return {
                    "data" : {
                        "token" : self.generate_access_token(normal_user.id, 'normal_user'),
                        "username" : normal_user.username,
                        "id" : normal_user.id,
                        "mobile_number" : normal_user.mobileNumber
                    }
                }
            except ObjectDoesNotExist:
                return {
                   "error" : {
                        "message" : 'sorry this user isn\'t exists',
                   }  
                }


