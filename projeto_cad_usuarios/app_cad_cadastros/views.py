from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')