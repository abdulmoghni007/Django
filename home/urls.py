from django.urls import path
from . import views

urlpatterns = [

    path('home',views.HomeView.as_view()),
    path('basicHome',views.basicHome),
    path('authorized', views.authorized.as_view()),
]