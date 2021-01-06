from django.urls import path
from .controllers import mange_promo , modify_promo 

app_name = 'Promo'

urlpatterns = [
    path('', mange_promo),
    path('<int:pk>', modify_promo),

]
