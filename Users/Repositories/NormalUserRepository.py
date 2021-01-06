from ..models import NormalUser
from django.core.exceptions import ObjectDoesNotExist

class NormalUserRepository : 

    def get_one_by_user_name(self,username):
        try:
            user = NormalUser.objects.get(username=username)
            return user
        except ObjectDoesNotExist:
             return False

    def get_one_by_id(self,id):
        try:
            user = NormalUser.objects.get(pk=id)
            return user
        except ObjectDoesNotExist:
             return False
