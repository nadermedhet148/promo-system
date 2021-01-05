import datetime
import jwt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class UsersService:

    def __init__(self,administratorUserRepository,normalUserRepository):
        self.normalUserRepository = normalUserRepository
        self.administratorUserRepository = administratorUserRepository


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
        administrator_user = self.administratorUserRepository.get_one_by_user_name(username)
        if administrator_user:
            return {
                "data" : {
                    "token" : self.generate_access_token(administrator_user.id, 'administrator_user'),
                    "username" : administrator_user.username,
                    "id" : administrator_user.id,
                }
            }
        else :
            return {
               "error" : {
                    "message" : 'sorry this user isn\'t exists',
               }  
            }
    def normal_user_login(self, username) :
            normal_user = self.normalUserRepository.get_one_by_user_name(username)
            if normal_user:
                return {
                    "data" : {
                        "token" : self.generate_access_token(normal_user.id, 'normal_user'),
                        "username" : normal_user.username,
                        "id" : normal_user.id,
                        "mobile_number" : normal_user.mobileNumber
                    }
                }
            else:
                return {
                   "error" : {
                        "message" : 'sorry this user isn\'t exists',
                   }  
                }


