# importando as bibliotecas necessárias
from multiprocessing import Process
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
        
    # criando a função para iniciar a escrita no arquivo de log
    def _iniciar_log(self):
        with open(self.arquivo_log, "w") as f:
            f.write("Log de execução do escalonador\n")

    def _registrar_log(self, mensagem):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        log_message = f"[{timestamp}] {mensagem}"
        print(log_message)
        with open(self.arquivo_log, "a") as f:
            f.write(log_message + "\n")

    def iniciar(self):
        for tarefa in self.tarefas:
            tarefa.iniciar()

        tempo_inicial = time.time()

        while self.tarefas:
            for tarefa in list(self.tarefas):
                if not tarefa.esta_vivo():
                    self._registrar_log(f"Tarefa {tarefa.nome} (PID {tarefa.pid}) já terminou.")
                    self.tarefas.remove(tarefa)
                    continue

                self._registrar_log(f"Executando {tarefa.nome} (PID {tarefa.pid})")

                try:
                    os.kill(tarefa.pid, signal.SIGCONT)
                except ProcessLookupError:
                    self._registrar_log(f"Erro: Processo {tarefa.pid} não encontrado (já finalizado).")
                    self.tarefas.remove(tarefa)
                    continue

                time.sleep(self.quantum)

                try:
                    os.kill(tarefa.pid, signal.SIGSTOP)
                except ProcessLookupError:
                    self._registrar_log(f"Erro ao parar: Processo {tarefa.pid} não encontrado.")
                    self.tarefas.remove(tarefa)

        tempo_total = time.time() - tempo_inicial
        self._registrar_log(f"Todas as tarefas concluídas em {tempo_total:.2f} segundos.")