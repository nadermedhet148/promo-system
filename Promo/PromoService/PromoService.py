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

    def modify_promo(self,promoId,promoAmount,startTime,endTime,isActive,description,editorType=''):
        if editorType != 'administrator_user' :
                return {
                "error" : "sorry you must be administrator_user to create promotion"
        }
        promo = self.promoRepository.get_one_by_id(promoId)        
        if not promo : 
            return {
                "error" : "sorry this promo user isn\'t existed"
            }
                
        if promoAmount < 0 :
            return {
                    "error" : "sorry promoAmount should be bigger than 0"
                }  
        if startTime > endTime : 
            return {
                "error" : "sorry startTime should be less than endTime"
            } 
        promo.promoAmount = promoAmount
        promo.startTime = startTime
        promo.endTime = endTime
        promo.isActive = isActive
        promo.description = description
        updatedPromo = self.promoRepository.update(promo)
        if not updatedPromo : 
            return {
                "error" : "sorry internal error happen while edit promotion"
            }        
        return {
            "data" : updatedPromo
        }

    def delete_promo(self,promoId,editorType=''):
        if editorType != 'administrator_user' :
                return {
                "error" : "sorry you must be administrator_user to create promotion"
        }
        promo = self.promoRepository.get_one_by_id(promoId)        
        if not promo : 
            return {
                "error" : "sorry this promo user isn\'t existed"
            }

        deletePromo = self.promoRepository.delete(promo)
        if not deletePromo : 
            return {
                "error" : "sorry internal error happen while delete promotion"
            }        
        return {
            "data" : deletePromo
        }

    def get_promos(self,normalUserId=None):
        promos = self.promoRepository.listing(normalUserId)
        if not promos : 
            return {
                "error" : "sorry internal error happen while get promotions"
            }        
        return {
            "data" : promos
        }      


    def get_promo(self,promoId):
        promo = self.promoRepository.get_one_by_id(promoId)
        if not promo : 
            return {
                "error" : "sorry internal error happen while get promotion"
            }        
        return {
            "data" : promo
        }   
   
    def update_promo_amount(self,promoId,deductedPromoAmount,editorType,userId):
        if editorType != 'normal_user' :
                return {
                "error" : "sorry you must be normal_user to create promotion"
        }
        if deductedPromoAmount < 0 :
            return {
                    "error" : "sorry deductedPromoAmount should be bigger than 0"
                }  
        promo = self.promoRepository.get_one_by_id(promoId)     

        if not promo : 
            return {
                "error" : "sorry this promo  isn\'t existed"
            }

        if promo.normalUser.id != userId : 
            return {
                "error" : "sorry this promo is not related to you"
            }
        if(promo.promoAmount - deductedPromoAmount < 0 ) :
            return {
                "error" : "sorry this promo quantity less than the deducted quantity"
            }
            
        promo.promoAmount = promo.promoAmount - deductedPromoAmount   

        updatedPromo = self.promoRepository.update(promo)
        print(updatedPromo)
        if not updatedPromo : 
            return {
                "error" : "sorry internal error happen while edit promotion"
            }        
        return {
            "data" : updatedPromo
        }