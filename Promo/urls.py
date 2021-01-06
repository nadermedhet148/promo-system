from django.urls import path
from .controllers import create_promo , modify_promo

app_name = 'Promo'

urlpatterns = [
    path('', create_promo, name="create_promo"),
    path('<int:pk>', modify_promo, name="modify_promo"),

]
