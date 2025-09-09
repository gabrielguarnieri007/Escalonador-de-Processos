class Processo:
    """Representa um processo com todos os seus atributos."""
    def __init__(self, id: int, nome: str, prioridade: int, ciclos_necessarios: int, recurso_necessario: str = None):
        self.id = id
        self.nome = nome
        self.prioridade = prioridade
        self.ciclos_necessarios = ciclos_necessarios
        self.recurso_necessario = recurso_necessario
        self.prioridade_original = prioridade

    def __str__(self):
        """Retorna uma representação em string formatada do processo."""
        return f"ID[{self.id}]-{self.nome}(P{self.prioridade}, {self.ciclos_necessarios} ciclos)"

class No:
    """Representa um nó (elo) da lista encadeada."""
    def __init__(self, processo: Processo):
        self.processo = processo
        self.proximo = None

class ListaDeProcessos:
    """Implementação de uma lista encadeada para gerenciar uma fila de processos."""
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self) -> bool:
        """Verifica se a lista está vazia. Retorna True se vazia, False caso contrário."""
        return self.inicio is None

    def adicionar_no_final(self, processo: Processo):
        """Adiciona um processo ao final da lista (operação O(1))."""
        novo_no = No(processo)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def remover_do_inicio(self) -> Processo:
        """Remove e retorna o processo do início da lista (operação O(1))."""
        if self.esta_vazia():
            return None
        processo_removido = self.inicio.processo
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
        return processo_removido

    def __str__(self) -> str:
        """Retorna a representação em string de toda a lista de processos."""
        if self.esta_vazia():
            return "[]"
        string_final = "["
        no_atual = self.inicio
        while no_atual is not None:
            string_final += str(no_atual.processo)
            if no_atual.proximo is not None:
                string_final += ", "
            no_atual = no_atual.proximo
        string_final += "]"
        return string_final