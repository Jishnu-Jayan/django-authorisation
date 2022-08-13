
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('register/logout/',views.logout,name='logout'),
    path('logout/',views.logout,name='logout'),
    path('application/',views.application, name='application'),
]
