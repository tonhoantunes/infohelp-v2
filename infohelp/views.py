from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "inicio.html")

def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.usuario = request.user  # Associa o curso ao usuário logado
            curso.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'criar_curso.html', {'form': form})


def listar_cursos(request):
    cursos = Curso.objects.all().order_by('-data_criacao')
    return render(request, 'cursos.html', {'cursos': cursos})

def biblioteca(request):
    return render(request, "biblioteca.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")