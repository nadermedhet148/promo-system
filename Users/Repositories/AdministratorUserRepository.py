from ..models import AdministratorUser
from django.core.exceptions import ObjectDoesNotExist

class AdministratorUserRepository : 

    def __init__(self):
        pass
    
    def get_one_by_user_name(self,username):
        try:
            administrator_user = AdministratorUser.objects.get(username=username)
            return administrator_user
        except ObjectDoesNotExist:
             return False
