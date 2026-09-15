# Escalonamento de Processos

Simulador de algoritmos de escalonamento de processos, desenvolvido para a disciplina de Sistemas Operacionais (IFRS Campus Restinga, 2026/2).

## Algoritmos implementados

- [x] FCFS
- [ ] SJF Não-Preemptivo
- [ ] SJF Preemptivo
- [ ] Prioridade Não-Preemptivo
- [ ] Prioridade Preemptivo
- [ ] Round-Robin

## Como executar

```bash
python base.py
```

O programa exibe um menu interativo para cadastrar processos (manual ou aleatório), escolher o algoritmo e visualizar o histórico de execução, tempo de espera e tempo médio de espera.

## Entrada de processos

Os atributos exigidos variam conforme o algoritmo:

- **FCFS**: tempo de execução.
- **SJF Não-Preemptivo**: tempo de execução, tempo de chegada.
- **SJF Preemptivo**: tempo de execução, tempo de chegada.
- **Prioridade Não-Preemptivo**: tempo de execução, tempo de chegada, prioridade.
- **Prioridade Preemptivo**: tempo de execução, tempo de chegada, prioridade.
- **Round-Robin**: tempo de execução.

## Tags de entrega

| Tag | Algoritmo |
|---|---|
| v1.0 | FCFS |
| v2.0 | SJF |
| v3.0 | Prioridade |
| v4.0 | Round-Robin |

---
README gerado com o auxílio de IA. Perplexity | Claude Sonnet 4.5.