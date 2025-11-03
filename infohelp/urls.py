from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),

    path('categorias/nova/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/deletar/', views.deletar_categoria, name='deletar_categoria'),

    path('cursos/novo/', views.criar_curso, name='criar_curso'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),

]