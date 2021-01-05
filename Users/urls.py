from django.urls import path
from .controllers import administrator_user_login,normal_user_login

app_name = 'Users'

urlpatterns = [
    path('administrator_user/auth', administrator_user_login, name="administrator_user_login"),
    path('normal_user/auth', normal_user_login, name="normal_user_login"),

]
