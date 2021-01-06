from django.contrib import admin
from .models import Promo

class PromoAdmin(admin.ModelAdmin):
    list_display = (
        "promoType",
        "promoCode",
        "creationTime",
        "startTime",
        "endTime",
        "promoAmount",
        "isActive",
        "description",
        "normalUser",
    )


admin.site.register(Promo, PromoAdmin)