
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    # path('dltacc',views.dltacc, name='dltacc'),

]