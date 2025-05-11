# importando as bibliotecas necessárias
import os
import time
from multiprocessing import Process
import signal
import random

# criando a classe Tarefa
class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.process = Process(target=self.trabalho)
        self.pid = None

    def trabalho(self):
        os.kill(os.getpid(), signal.SIGSTOP)  # Aguarda o escalonador liberar
        print(f"[{os.getpid()}] {self.nome} começando o trabalho...")
        tempo_total = random.randint(5, 10)
        for i in range(tempo_total):
            print(f"[{os.getpid()}] {self.nome}: trabalhando {i+1}/{tempo_total}")
            time.sleep(1)
        print(f"[{os.getpid()}] {self.nome} terminou o trabalho.")

    def iniciar(self):
        self.process.start()
        self.pid = self.process.pid

    def esta_ativa(self):
        return self.process.is_alive()

    def terminar(self):
        self.process.join()