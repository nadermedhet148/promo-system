from django.db import models



class AdministratorUser(models.Model):
    name = models.CharField(("Name"), max_length=255)
    username = models.CharField(("UserName"), max_length=255)
    address = models.CharField(("Address"), max_length=255)
    class Meta:
        verbose_name = "Administrator_User"
        verbose_name_plural = "Administrator_Users"

class NormalUser(models.Model):
    name = models.CharField(("Name"), max_length=255)
    username = models.CharField(("UserName"), max_length=255)
    address = models.CharField(("Address"), max_length=255)
    mobileNumber = models.CharField(("Mobile_Number"), max_length=255)

    class Meta:
        verbose_name = "Normal_User"
        verbose_name_plural = "Normal_Users"
