from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.http import HttpResponseForbidden
from .forms import CadastroForm, ProjetoForm
from .models import Voluntario,Usuario, Cacador, Message, Projeto
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


def teste(request):
    return render(request, 'paginas/teste.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'paginas/home.html')

@login_required(login_url='/login/')
def projetos(request):
    projetos = Projeto.objects.all()
    selected_state = request.GET.get('state_project')
    selected_city = request.GET.get('city_project')

    if selected_state:
        projetos = projetos.filter(estados=selected_state)
    if selected_city:
        projetos = projetos.filter(cidade=selected_city)

    unique_states = Projeto.objects.values_list('estados', flat=True).distinct()
    unique_cities = Projeto.objects.values_list('cidade', flat=True).distinct()

    context = {
        'projetos': projetos,
        'selected_state': selected_state,
        'selected_city': selected_city,
        'unique_states': unique_states,
        'unique_cities': unique_cities,
    }
    
    return render(request, 'paginas/projetos.html', context )

def projetoX(request):
    return HttpResponse("Projeto X")

def projetoY(request):
    return HttpResponse("Projeto Y")

def projetoW(request):
    return HttpResponse("Projeto W")

def projetoZ(request):
    return HttpResponse("Projeto Z")

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
    unique_states = Voluntario.objects.values_list('estado', flat=True).distinct()
    unique_cities = Voluntario.objects.values_list('cidade', flat=True).distinct()

    # Get the selected state and city from the request
    state = request.GET.get('state')
    city = request.GET.get('city')

    # Initially, set the queryset to all voluntarios
    voluntarios = Voluntario.objects.all()

    if state:
        voluntarios = voluntarios.filter(estado=state)

    if city:
        voluntarios = voluntarios.filter(cidade=city)

    context = {
        'voluntarios': voluntarios,
        'unique_states': unique_states,
        'unique_cities': unique_cities,
        'selected_state': state,
        'selected_city': city,
    }

    return render(request, 'paginas/voluntarios.html', context)

@login_required(login_url='/login/')
def chat_geral(request):
    users = User.objects.all()
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'paginas/chat_geral.html', {'users': users, 'messages': messages})

@login_required(login_url='/login/')
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        try:
            # Código para salvar a mensagem
            message = Message(sender=request.user, content=content)
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
    
@login_required(login_url='/login/')  
def cadastro_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()


    return render(request, 'paginas/cadastro_projetos.html', {'form': form})

@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    response = MessagingResponse()
    response.message('Yara é um genio!')
    return HttpResponse(str(response))