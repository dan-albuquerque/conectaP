from conectaplusapp.models import Cacador

class CacadorDAO:

    @staticmethod
    def obterTodosCacadores():
        cacadores = Cacador.objects.all()
        return cacadores
    