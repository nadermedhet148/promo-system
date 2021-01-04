from django.contrib import admin
from .models import AdministratorUser, NormalUser

class AdministratorUserAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "address")

class NormalUserAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "address", "mobileNumber")


admin.site.register(AdministratorUser, AdministratorUserAdmin)
admin.site.register(NormalUser, NormalUserAdmin)

