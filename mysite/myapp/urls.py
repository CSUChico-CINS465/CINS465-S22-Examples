from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path('', views.index),
    path('suggestions/', views.suggestion_view),
    path('suggestion/', views.add_suggestion_view),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.registration_view),
    path('logout/', views.logout_view),
    path('comment/<int:sugg_id>/', views.add_comment_view),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)