# importando as bibliotecas necessárias
import os
import time
import signal
from multiprocessing import Process

# criando a classe Tarefa
class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.processo = Process(target=self.trabalho)
        self.pid = None