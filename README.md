# Simulador de Escalonador Round Robin

Este projeto simula o funcionamento de um **escalonador Round Robin** utilizando *multiprocessamento* em Python. O escalonador gerencia tarefas que são executadas de forma concorrente, cada uma recebendo um tempo fixo de execução (quantum) antes de ser pausada para a próxima iniciar.

## Descrição do Projeto

A ideia principal é demonstrar como um escalonador do tipo Round Robin pode controlar tarefas de maneira cíclica, usando sinais do sistema operacional (`SIGSTOP` e `SIGCONT`) para pausar e retomar processos.

Cada tarefa simula uma operação que leva um tempo aleatório para ser concluída, imprimindo mensagens para mostrar seu progresso. O escalonador garante que todas as tarefas recebam tempo de CPU de maneira justa e alternada.

## Organização do Projeto

O código está organizado em três arquivos principais:

- `main.py`  
  Arquivo principal que inicializa o escalonador, cria as tarefas e inicia o processo de escalonamento.

- `tarefa.py`  
  Define a classe `Tarefa`, responsável por encapsular a lógica de execução de um processo filho. Cada tarefa começa em estado de espera (`SIGSTOP`) e só começa a trabalhar quando o escalonador a libera (`SIGCONT`).

- `escalonador.py`  
  Implementa a classe `Escalonador`, que gerencia a fila de tarefas, aplica o quantum e registra um log da execução (`log.txt`).

## Como Executar

1. **Pré-requisitos:**
   - Python 3.6 ou superior
   - Sistema operacional baseado em UNIX (Linux ou macOS) — devido ao uso de sinais como `SIGSTOP` e `SIGCONT`

2. **Clone o repositório (ou copie os arquivos para uma pasta):**

   ```bash
   git clone <url-do-repo>
   cd <pasta-do-projeto>
