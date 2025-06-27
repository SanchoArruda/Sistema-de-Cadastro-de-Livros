from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm, CategoriaForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


@login_required  # Decorador para garantir que o usuário esteja logado antes de acessar as views
# já existentes
@permission_required('livros.view_livro', raise_exception=True)  # Permissão para visualizar livros
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})

@login_required  
@permission_required('livros.add_livro', raise_exception=True)  
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/livros/')
    else:
        form = LivroForm()
    return render(request, 'livros/adicionar_livro.html', {'form': form})

@login_required  
def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'livros/detalhe.html', {'livro': livro})

@login_required  
@permission_required('livros.change_livro', raise_exception=True)  
def editar_livro(request, id):
    livro = Livro.objects.get(pk=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/livros/')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/adicionar_livro.html', {'form': form})

@login_required  
@permission_required('livros.delete_livro', raise_exception=True)
def deletar_livro(request, id):
    Livro.objects.get(id=id).delete()
    return HttpResponseRedirect('/livros/')

@login_required
@permission_required('livros.view_categoria', raise_exception=True)  
def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:adicionar_livro') 
    else:
        form = CategoriaForm()
    return render(request, 'livros/adicionar_categoria.html', {'form': form})
