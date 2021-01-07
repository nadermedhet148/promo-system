from django.urls import path
from .controllers import mange_promo , modify_promo , mange_user_promo

app_name = 'Promo'

urlpatterns = [
    path('', mange_promo),
    path('<int:pk>', modify_promo),
    path('users/<int:pk>', mange_user_promo),


]
