from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse 
from .forms import CadastroForm
from .models import Voluntario,Usuario
from .models import Cacador

def teste(request):
    return render(request, 'paginas/teste.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'paginas/home.html')

@login_required(login_url='/login/')
def projetos(request):
    return render(request, 'paginas/projetos.html')

@login_required(login_url='/login/')
def cacadores(request):
    cacadores = Cacador.objects.all()
    context = {'cacadores': cacadores}
    return render(request, 'paginas/caçadores.html', context)

@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'paginas/inicio.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            user = form.save() 
            usuario = Usuario(user=user, nome=user.username, sobrenome='', phone='', email=form.cleaned_data['email'], senha=user.password)
            usuario.save()
            usuario.save()
            return redirect('inicio')
    else:
        form = CadastroForm()
        
    return render(request, 'paginas/cadastro.html', {
        'form': form
    })

@login_required(login_url='/login/')
def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    context = {'voluntarios': voluntarios}
    return render(request, 'paginas/voluntarios.html', context)

@login_required(login_url='/login/')
def chat_geral(request):
    return render(request, 'paginas/chat_geral.html')

def login_user(request):
    request.user = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            #cria perfil
            print(f"user: {request.user}")
            if not Usuario.objects.filter(user=request.user):
                
                Usuario.objects.create(user=request.user, name=username)
            
            return redirect("home") #redirecionamento quando ele consegue dfazer o login
        else:
            messages.success(request, ("Erro no seu login"))
            return redirect('login')
    else:
        context = {'username': ''}
        return render(request, "paginas/login.html", context)