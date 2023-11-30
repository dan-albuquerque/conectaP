from conectaplusapp.models import Atividade

class AtividadeDAO:

    @staticmethod
    def obterTodasAtividades():
        atividades = Atividade.objects.all()
        return atividades
    
    @staticmethod
    def criarAtividade(usuario_atribuido, nome, descricao):
        atividade = Atividade(usuario_atribuido=usuario_atribuido, nome=nome, descricao=descricao)
        atividade.save()
        return atividade