from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')


    #return HttpResponse('Hello, world!')    