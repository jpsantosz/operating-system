# importando as classes criadas
from tarefa import Tarefa
from escalonador import Escalonador

def main():
    # Cria 4 tarefas
    tarefas = [
        Tarefa("Tarefa 1"),
        Tarefa("Tarefa 2"),
        Tarefa("Tarefa 3"),
        Tarefa("Tarefa 4")
    ]
    
    # Cria o escalonador com quantum de 4 segundos
    escalonador = Escalonador(tarefas, quantum=4)
    escalonador.iniciar()

if __name__ == "__main__":
    main()