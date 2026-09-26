"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.
"""

import random

MAXIMO_TEMPO_EXECUCAO = 65535

ID = "id"
TEMPO_EXECUCAO = "tempo_execucao"
TEMPO_CHEGADA = "tempo_chegada"
PRIORIDADE = "prioridade"
TEMPO_RESTANTE = "tempo_restante"
TEMPO_ESPERA = "tempo_espera"

# n_processos = 3


def main():
    n_processos = ler_numero_processos()
    processos = popular_processos(n_processos)
    imprime_processos(processos)

    while True:
        alg = int(input(
            "\nMENU:"
            "\n1. FCFS \n2. SJF Preemptivo \n3. SJF Nao Preemptivo"
            "\n4. Prioridade Preemptivo \n5. Prioridade Nao Preemptivo \n6. Round_Robin"
            "\n7. Imprime lista de processos \n8. Popular processos novamente \n9. Sair \nOpção: "))

        if alg == 1:  # FCFS
            FCFS(processos)

        elif alg == 2:  # SJF PREEMPTIVO
            SJF(processos, True)

        elif alg == 3:  # SJF NAO PREEMPTIVO
            SJF(processos, False)

        elif alg == 4:  # PRIORIDADE PREEMPTIVO
            PRIORIDADE(processos, True)

        elif alg == 5:  # PRIORIDADE NAO PREEMPTIVO
            PRIORIDADE(processos, False)

        elif alg == 6:  # Round_Robin
            Round_Robin(processos)

        elif alg == 7:  # IMPRIME CONTEUDO INICIAL DOS PROCESSOS
            imprime_processos(processos)

        elif alg == 8:  # REATRIBUI VALORES INICIAIS
            n_processos = ler_numero_processos()
            processos = popular_processos(n_processos)
            imprime_processos(processos)

        elif alg == 9:
            print("\nFim...")
            break

def ler_numero_processos():
    while True:
        quantidade = int(input("\nDigite a quantidade de processos [inteiro > zero]: "))

        if quantidade > 0:
            return quantidade

        print("Entrada inválida")


def popular_processos(n_processos):
    aleatorio = int(input("\nDigite 1 para gerar os processos automaticamente. \nDigite outro número para inserir os valores manualmente. \nOpção: "))

    processos = []

    for i in range(n_processos):
        # Popular Processos Aleatorio
        if aleatorio == 1:
            tempo_execucao = random.randint(1, 10)
            tempo_chegada = random.randint(1, 10)
            prioridade = random.randint(1, 15)
        # Popular Processos Manual
        else:
            tempo_execucao = int(input(f"\nDigite o tempo de execucao do processo[{i}]: "))
            tempo_chegada = int(input(f"Digite o tempo de chegada do processo[{i}]: "))
            prioridade = int(input(f"Digite a prioridade do processo[{i}]: "))

        processos.append({
            ID: i,
            TEMPO_EXECUCAO: tempo_execucao,
            TEMPO_CHEGADA: tempo_chegada,
            PRIORIDADE: prioridade,
            TEMPO_RESTANTE: tempo_execucao,
            TEMPO_ESPERA: 0
        })

    return processos


def imprime_processos(processos):
    # Imprime lista de processos
    print()
    for processo in processos:
        print(
            f"Processo[{processo[ID]}]: "
            f"tempo_execucao={processo[TEMPO_EXECUCAO]} "
            f"tempo_restante={processo[TEMPO_RESTANTE]} "
            f"tempo_chegada={processo[TEMPO_CHEGADA]} "
            f"prioridade={processo[PRIORIDADE]}"
        )


def imprime_stats(processos):
    # Implementar o calculo e impressao de estatisticas

    tempo_espera_total = 0.0

    print()

    for processo in processos:
        print(f"Processo[{processo[ID]}]: tempo_espera={processo[TEMPO_ESPERA]}")
        tempo_espera_total += processo[TEMPO_ESPERA]

    print(f"Tempo medio de espera: {tempo_espera_total / len(processos)}")


def FCFS(processos):
    processos_simulacao = [{**p} for p in processos]
    print("\n=== FCFS")

    processo_em_execucao = 0  # processo inicial no FIFO e o zero

    for tempo_atual in range(1, MAXIMO_TEMPO_EXECUCAO):
        processo = processos_simulacao[processo_em_execucao]

        print(f"tempo[{tempo_atual}]: processo[{processo[ID]}] restante={processo[TEMPO_RESTANTE]}")

        if processo[TEMPO_EXECUCAO] == processo[TEMPO_RESTANTE]:
            processo[TEMPO_ESPERA] = tempo_atual - 1

        if processo[TEMPO_RESTANTE] == 1:
            if processo_em_execucao == (len(processos_simulacao) - 1):
                break
            else:
                processo_em_execucao = processo_em_execucao + 1
        else:
            processo[TEMPO_RESTANTE] = processo[TEMPO_RESTANTE] - 1
    
    imprime_stats(processos_simulacao)


def SJF(processos, preemptivo):
    # consulta IA: criar cópia de dicionário preservando dados originais
    # desempacotamento de dicionário (**)
    processos_simulacao = [{**p} for p in processos]
    
    if preemptivo:
        print("\n=== SJF PREEMPTIVO")
        imprime_processos(processos_simulacao)
        print()

        processos_concluidos = 0
        processo_em_execucao = {}

        for tempo_atual in range(1, MAXIMO_TEMPO_EXECUCAO):
            processo_mais_curto = {}
            menor_tempo_restante = 11111 #refatorar

            if processo_em_execucao and processo_em_execucao[TEMPO_RESTANTE] > 0:
                processo_mais_curto = processo_em_execucao
                menor_tempo_restante = processo_mais_curto[TEMPO_RESTANTE]

            for processo in processos_simulacao:
                if (processo[TEMPO_CHEGADA] <= tempo_atual) and (processo[TEMPO_RESTANTE] > 0):
                    if processo[TEMPO_RESTANTE] < menor_tempo_restante:
                        menor_tempo_restante = processo[TEMPO_RESTANTE]
                        processo_mais_curto = processo

                    
            processo_em_execucao = processo_mais_curto

            if processo_em_execucao:
                print(f"tempo[{tempo_atual}]: processo[{processo_em_execucao[ID]}] restante={processo_em_execucao[TEMPO_RESTANTE]}")

                if processo_em_execucao[TEMPO_RESTANTE] == 1:
                    processo_em_execucao[TEMPO_RESTANTE] = 0
                    processo_em_execucao[TEMPO_ESPERA] = (tempo_atual + 1) - processo_em_execucao[TEMPO_CHEGADA] - processo_em_execucao[TEMPO_EXECUCAO]
                    processos_concluidos += 1

                    processo_em_execucao = {}
                    
                    if processos_concluidos == len(processos_simulacao):
                        break
                else:
                    processo_em_execucao[TEMPO_RESTANTE] -= 1
            else:
                print(f'tempo[{tempo_atual}]: CPU ociosa')

        imprime_stats(processos_simulacao)
                

        
    else:
        print("\n=== SJF NÃO PREEMPTIVO")
        imprime_processos(processos_simulacao)
        print()

        cpu_livre = True
        processos_concluidos = 0
        processo_em_execucao = {}

        for tempo_atual in range(1, MAXIMO_TEMPO_EXECUCAO):

            if cpu_livre:
                menor_tempo_execucao = 11111 #refatorar

                for processo in processos_simulacao:
                    if (processo[TEMPO_CHEGADA] <= tempo_atual) and (processo[TEMPO_RESTANTE] > 0):
                        if processo[TEMPO_EXECUCAO] < menor_tempo_execucao:
                            menor_tempo_execucao = processo[TEMPO_EXECUCAO]
                            processo_em_execucao = processo
                            cpu_livre = False        

            if not cpu_livre:
                print(f"tempo[{tempo_atual}]: processo[{processo_em_execucao[ID]}] restante={processo_em_execucao[TEMPO_RESTANTE]}")

                if processo_em_execucao[TEMPO_EXECUCAO] == processo_em_execucao[TEMPO_RESTANTE]:
                    processo_em_execucao[TEMPO_ESPERA] = tempo_atual - processo_em_execucao[TEMPO_CHEGADA]

                if processo_em_execucao[TEMPO_RESTANTE] == 1:
                    processo_em_execucao[TEMPO_RESTANTE] = 0
                    processos_concluidos += 1
                    cpu_livre = True #refatorar
                    processo_em_execucao = {}
                    
                    if processos_concluidos == len(processos_simulacao):
                        break
                else:
                    processo_em_execucao[TEMPO_RESTANTE] -= 1

            else:
                print(f'tempo[{tempo_atual}]: CPU ociosa')

        imprime_stats(processos_simulacao)        


def PRIORIDADE(processos, preemptivo):
    processos_simulacao = [{**p} for p in processos]

    # implementar codigo do Prioridade preemptivo e nao preemptivo
    # ...
    #


def Round_Robin(processos):
    processos_simulacao = [{**p} for p in processos]

    # implementar codigo do Round-Robin
    # ...
    #


main()
