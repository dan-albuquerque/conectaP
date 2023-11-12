from conectaplusapp.models import Message

class MessageDAO:
    @staticmethod
    def obterTodasMensagensOrdenadas():
        return Message.objects.all().order_by('timestamp')
    
    @staticmethod
    def criarMensagem(remetente, conteudo):
        mensagem = Message(sender=remetente, content=conteudo)
        mensagem.save()
        return mensagem