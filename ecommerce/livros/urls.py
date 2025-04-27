from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('<int:id>/', views.detalhe_livro, name='detalhe_livro'),
    path('edit/<int:id>/', views.editar_livro, name='editar_livro'),
    path('delete/<int:id>/', views.deletar_livro, name='deletar_livro'),
]
