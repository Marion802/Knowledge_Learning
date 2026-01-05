from django.urls import path
from .views import activate_account, register, user_login

urlpatterns = [
    path('activate/<uuid:token>/', activate_account, name='activate_account'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
