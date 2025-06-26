from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora
from .forms import EditoraForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def lista_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'editoras/lista_editoras.html', {'editoras': editoras})

@login_required
def adicionar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/editoras/')
    else:
        form = EditoraForm()
    return render(request, 'editoras/adicionar_editora.html', {'form': form})

@login_required
def detalhe_editora(request, id):
    editora = get_object_or_404(Editora, id=id)
    return render(request, 'editoras/detalhe.html', {'editora': editora})

@login_required
def editar_editora(request, id):
    editora = Editora.objects.get(pk=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/editoras/')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editoras/adicionar_editora.html', {'form': form})

@login_required
def deletar_editora(request, id):
    Editora.objects.get(id=id).delete()
    return HttpResponseRedirect('/editoras/')
    return render(request, 'editoras/deletar_editora.html', {'editora': editora})

