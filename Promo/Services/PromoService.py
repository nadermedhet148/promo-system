from datetime import datetime
from random import randint
from Users.Constants import USER_TYPES
from ..Constants import ERRORS_MESSAGES


class PromoService:

    def __init__(self, promoRepository, normalUserRepository):
        self.promoRepository = promoRepository
        self.normalUserRepository = normalUserRepository

    def create_promo(self, promoType, startTime, endTime, promoAmount, isActive, description, normalUserId, creatorType):
        normalUser = self.normalUserRepository.get_one_by_id(normalUserId)
        if creatorType != USER_TYPES.get('ADMINISTRATOR_USER'):
            return {
                "error":  ERRORS_MESSAGES.get('ADMINISTRATOR_USER_CREATE_PROMOTION')
            }
        if not normalUser:
            return {
                "error": ERRORS_MESSAGES.get('NORMAL_USER_NOT_EXISTED')
            }

        if promoAmount < 0:
            return {
                "error": ERRORS_MESSAGES.get('PROMOAMOUNT_LESS_THAN_ZERO')
            }
        if startTime > endTime:
            return {
                "error": ERRORS_MESSAGES.get('STARTTIME_LESS_THAN_ENDTIME')
            }
        newPromo = self.promoRepository.create_promo(promoType=promoType,
                                                     startTime=startTime,
                                                     endTime=endTime,
                                                     promoAmount=promoAmount,
                                                     isActive=True,
                                                     description=description,
                                                     normalUser=normalUser,
                                                     promoCode=randint(
                                                         1, 1000000)
                                                     )
        if not newPromo:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_CREATE_PROMOTION')
            }
        return {
            "data": newPromo
        }

    def modify_promo(self, promoId, promoAmount, startTime, endTime, isActive, description, editorType=''):
        if editorType != USER_TYPES.get('ADMINISTRATOR_USER'):
            return {
                "error": ERRORS_MESSAGES.get('ADMINISTRATOR_USER_MODIFY_PROMOTION')
            }
        promo = self.promoRepository.get_one_by_id(promoId)
        if not promo:
            return {
                "error": ERRORS_MESSAGES.get('PROMO_NOT_EXISTED')
            }

        if promoAmount < 0:
            return {
                "error": ERRORS_MESSAGES.get('PROMOAMOUNT_LESS_THAN_ZERO')
            }
        if startTime > endTime:
            return {
                "error":  ERRORS_MESSAGES.get('STARTTIME_LESS_THAN_ENDTIME')
            }
        promo.promoAmount = promoAmount
        promo.startTime = startTime
        promo.endTime = endTime
        promo.isActive = isActive
        promo.description = description
        updatedPromo = self.promoRepository.update(promo)
        if not updatedPromo:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_EDIT_PROMOTION')
            }
        return {
            "data": updatedPromo
        }

    def delete_promo(self, promoId, editorType=''):
        if editorType != USER_TYPES.get('ADMINISTRATOR_USER'):
            return {
                "error": ERRORS_MESSAGES.get("ADMINISTRATOR_USER_DELETE_PROMOTION")
            }
        promo = self.promoRepository.get_one_by_id(promoId)
        if not promo:
            return {
                "error": ERRORS_MESSAGES.get('PROMO_NOT_EXISTED')
            }

        deletePromo = self.promoRepository.delete(promo)
        if not deletePromo:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_DELETE_PROMOTION')
            }
        return {
            "data": deletePromo
        }

    def get_promos(self, normalUserId=None):
        promos = self.promoRepository.listing(normalUserId)
        if not promos:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_GET_PROMOTIONS')
            }
        return {
            "data": promos
        }

    def get_promo(self, promoId):
        promo = self.promoRepository.get_one_by_id(promoId)
        if not promo:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_GET_PROMOTION')
            }
        return {
            "data": promo
        }

    def update_promo_amount(self, promoId, deductedPromoAmount, editorType, userId):
        if editorType != USER_TYPES.get('NORMAL_USER'):
            return {
                "error": ERRORS_MESSAGES.get('NORMAL_USER_UPDATE_PROMOTION_AMOUNT')
            }
        if deductedPromoAmount < 0:
            return {
                "error": ERRORS_MESSAGES.get('DEDUCTEDPROMOAMOUNT_LESS_THAN_ZERO')
            }
        promo = self.promoRepository.get_one_by_id(promoId)

        if not promo:
            return {
                "error": ERRORS_MESSAGES.get('PROMO_NOT_EXISTED')
            }

        if promo.normalUser.id != userId:
            return {
                "error": ERRORS_MESSAGES.get('PROMO_NOT_RELATED_TO_YOU')
            }
        if(promo.promoAmount - deductedPromoAmount < 0):
            return {
                "error": ERRORS_MESSAGES.get('PROMO_QUANTITY_LESS_THAN_DEDUCTED_QUANTITY')
            }

        promo.promoAmount = promo.promoAmount - deductedPromoAmount

        updatedPromo = self.promoRepository.update(promo)
        print(updatedPromo)
        if not updatedPromo:
            return {
                "error": ERRORS_MESSAGES.get('INTERNAL_ERROR_EDIT_PROMOTION')
            }
        return {
            "data": updatedPromo
        }
