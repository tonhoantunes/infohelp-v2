from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),

    path('cursos/novo/', views.criar_curso, name='criar_curso'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),

]