from django.urls import path
from . import views

urlpatterns = [

    path('home',views.home),
    path('basicHome',views.basicHome),
    path('authorized', views.authorized),
]