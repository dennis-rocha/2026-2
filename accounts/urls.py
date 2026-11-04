from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('login/', views.login, name='login'),

    # Logout
    path('logout/', views.logout, name='logout'),

    # Create Users
    path('create-user/', views.create_user, name='create_user'),

    # Esqueci a senha
    
    
]
