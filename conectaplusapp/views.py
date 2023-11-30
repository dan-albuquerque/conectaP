from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.http import HttpResponseForbidden
from .forms import CadastroForm, ProjetoForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .daos.usuarioDAO import UsuarioDAO
from .daos.projetoDAO import ProjetoDAO
from .daos.usuarioDAO import UsuarioDAO
from .daos.cacadorDAO import CacadorDAO
from .daos.voluntarioDAO import VoluntarioDAO
from .daos.messageDAO import MessageDAO
from .daos.atividadeDAO import AtividadeDAO
from django.shortcuts import get_object_or_404
from .models import Projeto


def teste(request):
    return render(request, 'paginas/teste.html')

@login_required(login_url='/login/')
def home(request):
    atividadeDAO = AtividadeDAO()
    atividades = atividadeDAO.obterTodasAtividades()
    if request.method == 'POST':

        nova_atividade_nome = request.POST.get('nova_atividade_nome', '')
        if nova_atividade_nome:
            atividadeDAO.criarAtividade(usuario_atribuido=request.user, nome=nova_atividade_nome, descricao='')
            return redirect('home')
    context = {'atividades': atividades}
    return render(request, 'paginas/home.html', context)

@login_required(login_url='/login/')
def projetos(request):
    projetoDAO = ProjetoDAO()

    projetos = projetoDAO.obterTodosProjetos()
    
    selected_state = request.GET.get('state_project')
    selected_city = request.GET.get('city_project')

    if selected_state:
        projetos = projetoDAO.obterProjetosPorEstado(estados=selected_state) 
    if selected_city:
        projetos = projetoDAO.obterProjetosPorCidade(cidades=selected_city)

    unique_states = projetoDAO.obterEstadosDistintos()
    unique_cities = projetoDAO.obterCidadesDistintas()

    context = {
        'projetos': projetos,
        'selected_state': selected_state,
        'selected_city': selected_city,
        'unique_states': unique_states,
        'unique_cities': unique_cities,
    }
    
    return render(request, 'paginas/projetos.html', context )



@login_required(login_url='/login/')
def cacadores(request):
    cacadorDAO = CacadorDAO()

    cacadores = cacadorDAO.obterTodosCacadores()
    context = {'cacadores': cacadores}
    return render(request, 'paginas/caçadores.html', context)

@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'paginas/inicio.html')

def cadastro(request):
    usuarioDAO = UsuarioDAO()

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            usuarioDAO.criarUsuario(username, email, password) # se quiser pode colocar phone e email como parâmetro

            return redirect('inicio')
    else:
        form = CadastroForm()
        
    return render(request, 'paginas/cadastro.html', {
        'form': form
    })

@login_required(login_url='/login/')
def voluntarios(request):
    voluntarioDAO = VoluntarioDAO()

    unique_states = voluntarioDAO.obterVoluntariosPorEstado()
    unique_cities = voluntarioDAO.obterVoluntariosPorCidade()

    state = request.GET.get('state')
    city = request.GET.get('city')

    voluntarios = voluntarioDAO.obterTodosVoluntarios()

    if state:
        voluntarios = voluntarioDAO.obterVoluntariosPorEstado(estado=state)

    if city:
        voluntarios = voluntarioDAO.obterVoluntatiosPorCidade(cidade=city)

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
    usuarioDAO = UsuarioDAO()
    messageDAO = MessageDAO()

    users = usuarioDAO.obterTodosUsuarios()
    messages = messageDAO.obterTodasMensagensOrdenadas()
    return render(request, 'paginas/chat_geral.html', {'users': users, 'messages': messages})

@login_required(login_url='/login/')
def send_message(request):
    messageDAO = MessageDAO()

    if request.method == 'POST':
        conteudo = request.POST.get('message')
        try:
            mensagem = messageDAO.criarMensagem(remetente=request.user, conteudo=conteudo)
            return redirect('chat_geral')
        except Exception as e:
            return JsonResponse({'status': 'error', 'error_message': str(e)})

def login_user(request):
    usuarioDAO = UsuarioDAO()

    request.user = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Comentei pois acho que não faz sentido essa parte. Pois o Usuario sempre é criado no cadastro
            #cria perfil
            #print(f"user: {request.user}")
            #if not usuarioDAO.obterUsuarioPorUser(user=request.user):
            #    
            #    Usuario.objects.create(user=request.user, name=username)
            #
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
    response.message('Hostech')
    return HttpResponse(str(response))



def visualizar_projeto(request, id):
    # Busca o projeto pelo ID ou retorna um erro 404 se não encontrar
    projeto = get_object_or_404(Projeto, id=id)
    # Renderiza o template 'visualizar_projeto.html' passando o projeto encontrado como contexto
    # Note the 'paginas/' prefix in the template name
    return render(request, 'paginas/visualizar_projeto.html', {'projeto': projeto})

