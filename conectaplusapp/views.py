from django.shortcuts import render, redirect
from django.http.response import HttpResponse 
from .forms import CadastroForm
from .models import Voluntario
from .models import Cacador


def teste(request):
    
    return render(request, 'paginas/teste.html')

def home(request):
    return render(request, 'paginas/home.html')

def projetos(request):
    return render(request, 'paginas/projetos.html')

def cacadores(request):
    cacadores = Cacador.objects.all()
    context = {'cacadores': cacadores}
    return render(request, 'paginas/caçadores.html', context)

def inicio(request):
    return render(request, 'paginas/inicio.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            form.save()
    
            return redirect('login')
    else:
        form = CadastroForm()
        
    return render(request, 'paginas/cadastro.html', {
        'form': form
    })

def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    context = {'voluntarios': voluntarios}
    return render(request, 'paginas/voluntarios.html', context)

def chat_geral(request):
    return render(request, 'paginas/chat_geral.html')