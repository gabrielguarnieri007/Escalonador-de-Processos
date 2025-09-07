from estruturas import Processo, ListaDeProcessos

class Scheduler:
    def __init__(self):
        self.lista_alta_prioridade = ListaDeProcessos()
        self.lista_media_prioridade = ListaDeProcessos()
        self.lista_baixa_prioridade = ListaDeProcessos()
        self.lista_bloqueados = ListaDeProcessos()
        self.contador_ciclos_alta_prioridade = 0

    def adicionar_processo(self, processo: Processo):
        if processo.prioridade == 1:
            self.lista_alta_prioridade.adicionar_no_final(processo)
        elif processo.prioridade == 2:
            self.lista_media_prioridade.adicionar_no_final(processo)
        elif processo.prioridade == 3:
            self.lista_baixa_prioridade.adicionar_no_final(processo)