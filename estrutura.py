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