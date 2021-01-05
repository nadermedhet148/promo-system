from ..models import NormalUser
from django.core.exceptions import ObjectDoesNotExist

class NormalUserRepository : 

    def get_one_by_user_name(self,username):
        try:
            administrator_user = NormalUser.objects.get(username=username)
            return administrator_user
        except ObjectDoesNotExist:
             return False
