from django.urls import path
from . import views

app_name = 'editoras'

urlpatterns = [
    path('', views.lista_editoras, name='lista_editoras'),
    path('adicionar/', views.adicionar_editora, name='adicionar_editora'),
    path('<int:id>/', views.detalhe_editora, name='detalhe_editora'),
    path('edit/<int:id>/', views.editar_editora, name='editar_editora'),
    path('delete/<int:id>/', views.deletar_editora, name='deletar_editora'),
]
