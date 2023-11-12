from conectaplusapp.models import Voluntario

class VoluntarioDAO:
    @staticmethod
    def obterTodosVoluntarios():
        return Voluntario.objects.all()
    
    @staticmethod
    def obterVoluntariosPorEstado():
        return Voluntario.objects.values_list('estado', flat=True).distinct()
    
    @staticmethod
    def obterVoluntariosPorCidade():
        return Voluntario.objects.values_list('cidade', flat=True).distinct()
    
    @staticmethod
    def filtrarPorEstado(estado):
        return Voluntario.objects.filter(estado=estado)
    
    @staticmethod
    def filtrarPorCidade(cidade):
        return Voluntario.objects.filter(cidade=cidade)