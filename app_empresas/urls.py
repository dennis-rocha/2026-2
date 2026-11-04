from django.urls import path
from . import views

urlpatterns = [
    # CRUD
    
    # Create
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastrar_empresa'),
    
    # Read
    path('', views.home, name='empresas'),
    
    # Update
    path('atualizar_empresa/<int:id>/', views.atualizar_empresa, name="atualizar_empresa"),
    
    # Delete
    path('remover_empresa/<int:id>/', views.remover_empresa, name='remover_empresa'),
    
    
]
