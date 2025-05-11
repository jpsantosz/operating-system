from escalonador import Escalonador
from tarefa import Tarefa

def main():
    escalonador = Escalonador(quantum=2)

    tarefa1 = Tarefa("Tarefa 1")
    tarefa2 = Tarefa("Tarefa 2")
    tarefa3 = Tarefa("Tarefa 3")
    tarefa4 = Tarefa("Tarefa 4")

    escalonador.adicionar_tarefa(tarefa1)
    escalonador.adicionar_tarefa(tarefa2)
    escalonador.adicionar_tarefa(tarefa3)
    escalonador.adicionar_tarefa(tarefa4)

    escalonador.iniciar()

if __name__ == "__main__":
    main()
