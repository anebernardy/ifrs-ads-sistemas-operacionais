"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.

Codigo-base em Python. Equivalente ao base.java, com a mesma estrutura de dados
(listas paralelas), o mesmo menu e a mesma saida.

O FCFS ja vem implementado como exemplo de referencia.
Cabe a voce implementar: SJF (preemptivo e nao preemptivo), Prioridade
(preemptivo e nao preemptivo) e Round Robin.
"""

import random

MAXIMO_TEMPO_EXECUCAO = 65535

# n_processos = 3


def main():
    n_processos = ler_numero_processos()

    tempo_execucao = [0] * n_processos
    tempo_chegada = [0] * n_processos
    prioridade = [0] * n_processos
    tempo_espera = [0] * n_processos
    tempo_restante = [0] * n_processos

    popular_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

    imprime_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

    # Escolher algoritmo
    while True:
        alg = int(input(
            "\nMENU:"
            "\n1. FCFS \n2. SJF Preemptivo \n3. SJF Nao Preemptivo"
            "\n4. Prioridade Preemptivo \n5. Prioridade Nao Preemptivo \n6. Round_Robin"
            "\n7. Imprime lista de processos \n8. Popular processos novamente \n9. Sair \nOpção: "))

        if alg == 1:  # FCFS
            FCFS(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 2:  # SJF PREEMPTIVO
            SJF(n_processos, True, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 3:  # SJF NAO PREEMPTIVO
            SJF(n_processos, False, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 4:  # PRIORIDADE PREEMPTIVO
            PRIORIDADE(n_processos, True, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 5:  # PRIORIDADE NAO PREEMPTIVO
            PRIORIDADE(n_processos, False, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 6:  # Round_Robin
            Round_Robin(n_processos, tempo_execucao, tempo_espera, tempo_restante)

        elif alg == 7:  # IMPRIME CONTEUDO INICIAL DOS PROCESSOS
            imprime_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 8:  # REATRIBUI VALORES INICIAIS
            n_processos = ler_numero_processos()
            popular_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)
            imprime_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 9:
            print("\nFim...")
            break

def ler_numero_processos():
    while True:
        quantidade = int(input("\nDigite a quantidade de processos [inteiro > zero]: "))

        if quantidade > 0:
            return quantidade

        print("Entrada inválida")


def popular_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade):
    aleatorio = int(input("\nDigite 1 para gerar os processos automaticamente. \nDigite outro número para inserir os valores manualmente. \nOpção: "))

    for i in range(n_processos):
        # Popular Processos Aleatorio
        if aleatorio == 1:
            tempo_execucao[i] = random.randint(1, 10)
            tempo_chegada[i] = random.randint(1, 10)
            prioridade[i] = random.randint(1, 15)
        # Popular Processos Manual
        else:
            tempo_execucao[i] = int(input("\nDigite o tempo de execucao do processo[" + str(i) + "]:  "))
            tempo_chegada[i] = int(input("Digite o tempo de chegada do processo[" + str(i) + "]:  "))
            prioridade[i] = int(input("Digite a prioridade do processo[" + str(i) + "]:  "))

        tempo_restante[i] = tempo_execucao[i]
        tempo_espera[i] = 0


def imprime_processos(n_processos, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade):
    # Imprime lista de processos
    print()
    for i in range(n_processos):
        print("Processo[" + str(i) + "]: tempo_execucao=" + str(tempo_execucao[i]) +
              " tempo_restante=" + str(tempo_restante[i]) +
              " tempo_chegada=" + str(tempo_chegada[i]) +
              " prioridade =" + str(prioridade[i]))


def imprime_stats(n_processos, espera):
    tempo_espera = list(espera)
    # Implementar o calculo e impressao de estatisticas

    tempo_espera_total = 0.0

    print()
    for i in range(n_processos):
        print("Processo[" + str(i) + "]: tempo_espera=" + str(tempo_espera[i]))
        tempo_espera_total = tempo_espera_total + tempo_espera[i]

    print("Tempo medio de espera: " + str(tempo_espera_total / n_processos))


def FCFS(n_processos, execucao, espera, restante, chegada):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    # tempo_chegada = list(chegada)

    processo_em_execucao = 0  # processo inicial no FIFO e o zero

    print("\n=== FCFS")

    # implementar codigo do FCFS
    for i in range(1, MAXIMO_TEMPO_EXECUCAO):
        print("tempo[" + str(i) + "]: processo[" + str(processo_em_execucao) + "] restante=" +
              str(tempo_restante[processo_em_execucao]))

        if tempo_execucao[processo_em_execucao] == tempo_restante[processo_em_execucao]:
            tempo_espera[processo_em_execucao] = i - 1

        if tempo_restante[processo_em_execucao] == 1:
            if processo_em_execucao == (n_processos - 1):
                break
            else:
                processo_em_execucao = processo_em_execucao + 1
        else:
            tempo_restante[processo_em_execucao] = tempo_restante[processo_em_execucao] - 1
    #

    imprime_stats(n_processos, tempo_espera)


def SJF(n_processos, preemptivo, execucao, espera, restante, chegada):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)

    # implementar codigo do SJF preemptivo e nao preemptivo
    # ...
    #

    imprime_stats(n_processos, tempo_espera)


def PRIORIDADE(n_processos, preemptivo, execucao, espera, restante, chegada, prioridade):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)
    prioridade_temp = list(prioridade)

    # implementar codigo do Prioridade preemptivo e nao preemptivo
    # ...
    #

    imprime_stats(n_processos, tempo_espera)


def Round_Robin(n_processos, execucao, espera, restante):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)

    # implementar codigo do Round-Robin
    # ...
    #

    imprime_stats(n_processos, tempo_espera)


main()
