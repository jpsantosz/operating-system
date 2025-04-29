# importando as bibliotecas necessárias
import os
import time
import signal

# criando a classe do Escalonador 
class Escalonador:
    def __init__(self, tarefas, quantum, arquivo_log='log.txt'):
        self.tarefas = tarefas
        self.quantum = quantum
        self.arquivo_log = arquivo_log
        self._iniciar_log()