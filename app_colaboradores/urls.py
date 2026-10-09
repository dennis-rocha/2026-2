from django.urls import path
from . import views

urlpatterns = [
    # CRUD
    
    # Create
    path('cadastro_colaborador/', views.cadastro_colaborador, name='cadastrar_colaborador'),
    
    # Read
    path('', views.home, name='colaboradores'),
    
    # Update
    path('atualizar_colaborador/<int:id>/', views.atualizar_colaborador, name="atualizar_colaborador"),
    
    # Delete
    path('remover_colaborador/<int:id>/', views.remover_colaborador, name='remover_colaborador'),
    
    
]
