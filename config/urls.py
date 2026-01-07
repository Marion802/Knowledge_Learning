
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),   # 👈 URL racine
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path(
    'logout/',
    LogoutView.as_view(next_page='/'),
    name='logout'
    ),
]
