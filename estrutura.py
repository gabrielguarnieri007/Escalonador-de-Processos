class Processo:
    def __init__(self, id: int, nome: str, prioridade: int, ciclos_necessarios: int, recurso_necessario: str = None):
        self.id = id
        self.nome = nome
        self.prioridade = prioridade
        self.ciclos_necessarios = ciclos_necessarios
        self.recurso_necessario = recurso_necessario
        self.prioridade_original = prioridade

    def __str__(self):
        return f"ID[{self.id}]-{self.nome}(P{self.prioridade}, {self.ciclos_necessarios} ciclos)"
    class No:
    def __init__(self, processo: Processo):
        self.processo = processo
        self.proximo = None
        class ListaDeProcessos:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self) -> bool:
        return self.inicio is None
    # Adicionar este método dentro da classe ListaDeProcessos
    def adicionar_no_final(self, processo: Processo):
        novo_no = No(processo)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no