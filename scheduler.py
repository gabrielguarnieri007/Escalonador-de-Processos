

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
        return not (self.lista_alta_prioridade.esta_vazia() and
                    self.lista_media_prioridade.esta_vazia() and
                    self.lista_baixa_prioridade.esta_vazia() and
                    self.lista_bloqueados.esta_vazia())

    def executarCicloDeCPU(self):
        
        if not self.lista_bloqueados.esta_vazia():
            processo_desbloqueado = self.lista_bloqueados.remover_do_inicio()
            print(f"EVENTO: Processo '{processo_desbloqueado.nome}' foi desbloqueado e retornou para a fila P{processo_desbloqueado.prioridade_original}.")
            if processo_desbloqueado.prioridade_original == 1:
                self.lista_alta_prioridade.adicionar_no_final(processo_desbloqueado)
            elif processo_desbloqueado.prioridade_original == 2:
                self.lista_media_prioridade.adicionar_no_final(processo_desbloqueado)
            else:
                self.lista_baixa_prioridade.adicionar_no_final(processo_desbloqueado)

        
        processo_a_executar = None
        lista_de_origem = None

        if self.contador_ciclos_alta_prioridade >= 5:
            print("AVISO: Regra de anti-inanição ativada.")
            if not self.lista_media_prioridade.esta_vazia():
                processo_a_executar = self.lista_media_prioridade.remover_do_inicio()
                lista_de_origem = self.lista_media_prioridade
            elif not self.lista_baixa_prioridade.esta_vazia():
                processo_a_executar = self.lista_baixa_prioridade.remover_do_inicio()
                lista_de_origem = self.lista_baixa_prioridade
            if processo_a_executar:
                self.contador_ciclos_alta_prioridade = 0

        if processo_a_executar is None:
            if not self.lista_alta_prioridade.esta_vazia():
                processo_a_executar = self.lista_alta_prioridade.remover_do_inicio()
                lista_de_origem = self.lista_alta_prioridade
            elif not self.lista_media_prioridade.esta_vazia():
                processo_a_executar = self.lista_media_prioridade.remover_do_inicio()
                lista_de_origem = self.lista_media_prioridade
            elif not self.lista_baixa_prioridade.esta_vazia():
                processo_a_executar = self.lista_baixa_prioridade.remover_do_inicio()
                lista_de_origem = self.lista_baixa_prioridade

        
        if processo_a_executar:
            if processo_a_executar.recurso_necessario == "DISCO":
                print(f"EVENTO: Processo '{processo_a_executar.nome}' precisa de 'DISCO'. Movendo para bloqueados.")
                processo_a_executar.recurso_necessario = None 
                self.lista_bloqueados.adicionar_no_final(processo_a_executar)
            else:
                print(f"EXECUTANDO: {processo_a_executar}")
                processo_a_executar.ciclos_necessarios -= 1
                if lista_de_origem == self.lista_alta_prioridade:
                    self.contador_ciclos_alta_prioridade += 1
                if processo_a_executar.ciclos_necessarios <= 0:
                    print(f"EVENTO: Processo '{processo_a_executar.nome}' concluído e removido do sistema.")
                else:
                    lista_de_origem.adicionar_no_final(processo_a_executar)
        else:
            print("CPU OCIOSA: Nenhum processo para executar.")