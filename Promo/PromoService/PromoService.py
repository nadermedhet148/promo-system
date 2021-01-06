from datetime import datetime
from random import randint

class PromoService:

    def __init__(self,promoRepository,normalUserRepository):
        self.promoRepository=promoRepository
        self.normalUserRepository=normalUserRepository


    def create_promo(self,promoType,startTime,endTime,promoAmount,isActive,description,normalUserId,creatorType):
        normalUser = self.normalUserRepository.get_one_by_id(normalUserId)
        if creatorType != 'administrator_user' :
            return {
                "error" : "sorry you must be administrator_user to create promotion"
            }
        if not normalUser : 
            return {
                "error" : "sorry this normal user isn\'t existed"
            }
        
        if promoAmount < 0 :
            return {
                    "error" : "sorry promoAmount should be bigger than 0"
                }  
        if startTime > endTime : 
            return {
                "error" : "sorry startTime should be less than endTime"
            } 
        newPromo = self.promoRepository.create_promo(promoType=promoType,
                                                     startTime=startTime,
                                                     endTime=endTime,
                                                     promoAmount=promoAmount,
                                                     isActive=True,
                                                     description=description,
                                                     normalUser=normalUser,
                                                     promoCode=randint(1,1000000)
                                                    )
        if not newPromo : 
            return {
                "error" : "sorry internal error happen while create promotion"
            }        
        return {
            "data" : newPromo
        }