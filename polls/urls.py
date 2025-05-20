from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_page, name='login'),
    path('accounts/logout/', views.logout_page, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/password_reset/', views.password_reset, name='password reset'),
    path('accounts/password_reset_sent/', views.password_reset_sent, name='password reset sent'),
    path('survey/<str:pk>', views.survey, name='survey'),
    path('ai_survey/', views.ai_survey, name='ai_survey')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)














