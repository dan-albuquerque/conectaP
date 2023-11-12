from conectaplusapp.models import Usuario
from django.contrib.auth.models import User

class UsuarioDAO:

    @staticmethod
    def criarUsuario(username, email, password, sobrenome='', phone=''):
        user = User.objects.create_user(username, email, password)

        usuario = Usuario(
            user=user,
            nome=user.username,
            sobrenome=sobrenome,
            phone=phone,
            email=email,
            senha=password
        )
        
        usuario.save()

        return usuario

    @staticmethod
    def obterTodosUsuarios():
        return Usuario.objects.all()
    
    @staticmethod
    def obterUsuarioPorUser(user):
        return Usuario.objects.filter(user=user)

