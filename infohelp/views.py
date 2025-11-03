from django.shortcuts import render, redirect
from .models import Curso, Categoria
from .forms import CursoForm, CategoriaForm

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'criar_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

def deletar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'deletar_categoria.html', {'categoria': categoria})




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