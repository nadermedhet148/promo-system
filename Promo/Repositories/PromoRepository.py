from ..models import Promo
from django.core.exceptions import ObjectDoesNotExist


class PromoRepository :
    def __init__(self):
            pass
    
    def create_promo(self,promoType,promoCode,startTime,endTime,promoAmount,isActive,description,normalUser):
        # try:
        promo = Promo.objects.create(promoAmount=promoAmount,promoCode=promoCode,promoType=promoType,startTime=startTime,endTime=endTime,isActive=isActive,description=description,normalUser=normalUser)
        return promo
        # except Exception:
        #      return False

    def get_one_by_id(self,id):
        try:
            promo = Promo.objects.get(pk=id)
            return promo
        except ObjectDoesNotExist:
             return False

    def delete(self,promo):
        try:
            promo.delete()
            return promo
        except Exception:
             return False
    def update(self,promo):
        try:
            promo.save()
            return promo
        except Exception:
             return False

    def listing(self,normalUserId=None):
        try:
            if not normalUserId:
                promos = Promo.objects.all()
            if normalUserId :
                promos = Promo.objects.filter(normalUser=normalUserId)
            return promos
        except Exception:
             return False