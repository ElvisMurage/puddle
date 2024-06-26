from django.views.generic import TemplateView


from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name= 'core'

urlpatterns = [
     path('', views.index, name='index'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
     path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('signup/', views.signup, name='signup'),
     path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),name='login'),
]
