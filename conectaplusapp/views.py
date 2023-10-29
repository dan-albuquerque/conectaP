from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from .forms import CadastroForm
from .models import Voluntario,Usuario, Cacador, Message
from django.contrib.auth.models import User
from django.db.models import Q

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
    users = User.objects.all()
    selected_user_id = request.POST.get('selected_user')
    
    if selected_user_id:
        selected_user = User.objects.get(id=selected_user_id)
        messages = Message.objects.filter(
            Q(sender=selected_user, receiver=request.user) | Q(sender=request.user, receiver=selected_user)
        ).order_by('timestamp')
    else:
        messages = Message.objects.filter(
            Q(sender=request.user, receiver=request.user)
        ).order_by('timestamp')
    return render(request, 'paginas/chat_geral.html', {'users': users, 'messages': messages})


@login_required(login_url='/login/')
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        receiver_id = request.POST.get('receiver_id')  # Você precisa saber para quem enviar a mensagem
    try:
        # Código para salvar a mensagem
        message = Message(sender=request.user, receiver_id=receiver_id, content=content)
        message.save()
        return redirect('chat_geral')
    except Exception as e:
        return JsonResponse({'status': 'error', 'error_message': str(e)})

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