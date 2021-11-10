from django.contrib import admin
from django.urls import path

from .views import IndexView, register, login_user, logout_user

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
