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
            # Adicionar estes métodos dentro da classe Scheduler
def imprimir_estado_geral(self):
    print("\n--- ESTADO ATUAL DO ESCALONADOR ---")
    print(f"Alta Prioridade : {self.lista_alta_prioridade}")
    print(f"Média Prioridade: {self.lista_media_prioridade}")
    print(f"Baixa Prioridade: {self.lista_baixa_prioridade}")
    print(f"Bloqueados      : {self.lista_bloqueados}")
    print(f"Contador Anti-Inanição: {self.contador_ciclos_alta_prioridade}")
    print("-" * 50)

def tem_processos_pendentes(self):
    return not (self.lista_alta_prioridade.esta_vazia() and
                self.lista_media_prioridade.esta_vazia() and
                self.lista_baixa_prioridade.esta_vazia() and
                self.lista_bloqueados.esta_vazia())