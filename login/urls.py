from django.urls import path
from . import views

urlpatterns = [
    # functions to call by urls
    
    path('', views.home),

    path('login/', views.login),
    path('register/', views.register),
    path('connected/', views.connected),
    path('administration/', views.admin),

]