# importando as bibliotecas necessárias
import os
import time
import signal
from multiprocessing import Process
import random

# criando a classe Tarefa
class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.processo = Process(target=self.trabalho)
        self.pid = None
        
    def iniciar(self):
        self.processo.start()
        self.pid = self.processo.pid
        print(f"[TAREFA] {self.nome} iniciada com PID {self.pid}")

    def trabalho(self):
        print(f"[{os.getpid()}] {self.nome} começando o trabalho...")
        tempo_total = random.randint(5, 10)  # Simula tempos diferentes de trabalho
        for i in range(tempo_total):
            print(f"[{os.getpid()}] {self.nome}: trabalhando {i+1}/{tempo_total}")
            time.sleep(1)
        print(f"[{os.getpid()}] {self.nome} terminou o trabalho.")

    def esta_vivo(self):
        return self.processo.is_alive()

    def terminar(self):
        if self.esta_vivo():
            self.processo.terminate()
            self.processo.join()