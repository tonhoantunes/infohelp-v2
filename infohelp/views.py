from django.shortcuts import render
from .models import Curso

def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "inicio.html")

def listar_cursos(request):
    cursos = Curso.objects.all().order_by('-data_criacao')
    return render(request, 'cursos.html', {'cursos': cursos})

def biblioteca(request):
    return render(request, "biblioteca.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")