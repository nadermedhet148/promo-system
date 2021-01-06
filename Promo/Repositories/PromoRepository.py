from ..models import Promo


class PromoRepository :
    def __init__(self):
            pass
    
    def create_promo(self,promoType,promoCode,startTime,endTime,promoAmount,isActive,description,normalUser):
        try:
            promo = Promo.objects.create(promoAmount=promoAmount,promoCode=promoCode,promoType=promoType,startTime=startTime,endTime=endTime,isActive=isActive,description=description,normalUser=normalUser)
            return promo
        except Exception:
             return False
