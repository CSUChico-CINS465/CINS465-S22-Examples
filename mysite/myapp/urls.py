from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.index),
    path('suggestions/', views.suggestion_view),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.registration_view),
    path('logout/', views.logout_view),
]