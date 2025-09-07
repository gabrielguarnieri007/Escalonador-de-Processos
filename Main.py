import sys
import time
from scheduler import Scheduler
from estruturas import Processo

def carregar_processos_de_arquivo(nome_arquivo: str) -> list[Processo]:
    processos = []
    try:
        with open(nome_arquivo, 'r') as f:
            next(f) # Pula a primeira linha (cabeçalho)
            for linha in f:
                if not linha.strip():
                    continue
                partes = linha.strip().split(',')
                p = Processo(
                    id=int(partes[0]),
                    nome=partes[1],
                    prioridade=int(partes[2]),
                    ciclos_necessarios=int(partes[3]),
                    recurso_necessario=partes[4] if len(partes) > 4 and partes[4] else None
                )
                processos.append(p)
    except FileNotFoundError:
        return None
    return processos