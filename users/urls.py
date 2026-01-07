from django.urls import path
from .views import activate_account, register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('activate/<uuid:token>/', activate_account, name='activate_account'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
