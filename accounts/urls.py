from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]