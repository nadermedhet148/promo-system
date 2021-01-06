from django.urls import path
from .controllers import create_promo

app_name = 'Promo'

urlpatterns = [
    path('', create_promo, name="create_promo"),
]
