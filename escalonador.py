# importando as bibliotecas necessárias
import os
import time
import signal
from tarefa import Tarefa

class Escalonador:
    def __init__(self, quantum=2, log_path='log.txt'):
        self.quantum = quantum
        self.tarefas = []
        self.fila = []
        self.log_path = log_path

        # abrir o arquivo txt
        with open(self.log_path, 'w') as f:
            f.write("Log de execução do escalonador: \n")

    # adiciona as tarefas na lista de tarefas
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def iniciar(self):
        for tarefa in self.tarefas:
            tarefa.iniciar()
            self.fila.append(tarefa)

        # Dá tempo para os processos entrarem em SIGSTOP
        time.sleep(1)

        while self.fila:
            tarefa = self.fila.pop(0)

            if not tarefa.esta_ativa():
                continue  # processo já terminou

            os.kill(tarefa.pid, signal.SIGCONT)
            self.registrar_log(f"Executando {tarefa.nome} (PID {tarefa.pid})")
            time.sleep(self.quantum)
            os.kill(tarefa.pid, signal.SIGSTOP)

            if tarefa.esta_ativa():
                self.fila.append(tarefa)
            else:
                tarefa.terminar()

        self.registrar_log("Todas as tarefas foram concluídas.")

    def registrar_log(self, mensagem):
        timestamp = time.strftime("[%H:%M:%S]")
        print(f"{timestamp} {mensagem}")
        
        with open(self.log_path, 'a') as f:
            f.write(f"{timestamp} {mensagem}\n")
