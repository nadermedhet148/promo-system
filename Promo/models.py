from django.db import models
from django.utils.timezone import now
from Users.models import NormalUser
class Promo(models.Model):
    promoType = models.CharField(("Promo_Type"), max_length=255)
    promoCode = models.IntegerField(("Promo_Code"), unique=True)
    creationTime = models.DateField(("Creation_Time"),default=now, editable=False )
    startTime = models.DateField(("Start_Time"))
    endTime = models.DateField(("End_Time"))
    promoAmount = models.IntegerField(("Promo_Amount"))
    isActive = models.BooleanField(("Is_Active"), default=True)
    description = models.TextField(("Description"))
    normalUser = models.ForeignKey(NormalUser, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Promo"
        verbose_name_plural = "Promos"