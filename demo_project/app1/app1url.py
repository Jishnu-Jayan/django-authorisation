from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('',views.fun1),
    path('register/',views.register,name='register'),
    url('register/login/',views.login,name='login'),
    path('register/logout/',views.logout,name='logout'),
]
