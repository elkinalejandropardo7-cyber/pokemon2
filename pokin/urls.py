from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listar'),
    path('crear/', views.crear_pokemon, name='poken'),
    path('editar/<str:nombre>/', views.editar_pokemon, name='editar_pokemon'),
    path('eliminar/<str:nombre>/', views.eliminar, name='eliminar'),
]