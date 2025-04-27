from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.http import HttpResponseRedirect

# já existentes
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/livros/')
    else:
        form = LivroForm()
    return render(request, 'livros/adicionar_livro.html', {'form': form})

# NOVAS views
def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'livros/detalhe.html', {'livro': livro})

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

def deletar_livro(request, id):
    Livro.objects.get(id=id).delete()
    return HttpResponseRedirect('/livros/')
    return render(request, 'livros/deletar_livro.html', {'livro': livro})

