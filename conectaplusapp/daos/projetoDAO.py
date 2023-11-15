from conectaplusapp.models import Projeto

class ProjetoDAO:
    @staticmethod
    def obterTodosProjetos():
        return Projeto.objects.all()
    
    @staticmethod
    def obterEstadosDistintos():
        return Projeto.objects.values_list('estados', flat=True).distinct()
    
    @staticmethod
    def obterCidadesDistintas():
        return Projeto.objects.values_list('cidade', flat=True).distinct()
    
    @staticmethod
    def filtrarPorEstado(estado):
        return Projeto.objects.filter(estados=estado)
    
    @staticmethod
    def filtrarPorCidade(cidade):
        return Projeto.objects.filter(cidade=cidade)
    
    @staticmethod
    def obterProjetoPorId(self, id):
        return Projeto.objects.get(id=id)
