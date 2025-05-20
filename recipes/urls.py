from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('check-password/', views.check_password, name='check_password'),
    path('set-nickname/', views.set_nickname, name='set_nickname'),
]
