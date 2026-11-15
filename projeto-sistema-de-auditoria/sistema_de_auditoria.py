# -*- coding: utf-8 -*-
"""Sistema de Auditoria de Recursos Corporativos

Calcula o orçamento total de uma empresa organizada em dicionários
aninhados, com setores ignorados e conversão de moeda opcionais.

Autor: Matheus Montagner
"""

import time


# Auditoria: decorator que registra os parâmetros e o tempo de execução
def auditor(func):
    def auditoria(*args, **kwargs):
        print("=" * 45)
        print("INICIANDO AUDITORIA FINANCEIRA")
        print(f"Função auditada: {func.__name__}")
        print(f"Setores ignorados: {', '.join(args[1:]) or 'nenhum'}")
        print(f"Parâmetros extras: {kwargs or 'nenhum'}")

        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()

        print(f"Tempo de execução: {(fim - inicio) * 1000:.3f} ms")
        print("AUDITORIA CONCLUÍDA")
        print("=" * 45)
        return resultado

    return auditoria


# Estrutura da empresa: unidade -> setor -> área -> orçamento (em USD)
empresa = {
    "Matriz": {
        "TI": {
            "Infraestrutura": 50000,
            "Desenvolvimento": 80000,
            "Seguranca": 30000
        },
        "RH": {
            "Recrutamento": 20000,
            "Treinamento": 15000
        },
        "Financeiro": {
            "Contabilidade": 25000,
            "Auditoria": 18000
        }
    },
    "Filial": {
        "TI": {
            "Suporte": 22000
        },
        "Marketing": {
            "Publicidade": 40000,
            "Eventos": 12000
        }
    }
}


# Recursão
@auditor
def calcular_orcamento(estrutura, *departamentos_ignorados, **kwargs):
    taxa_cambio = kwargs.get("taxa_cambio", 1)
    moeda_destino = kwargs.get("moeda_destino", "USD")

    def soma_recursiva(no):
        total = 0
        for chave, valor in no.items():
            if chave in departamentos_ignorados:
                print(f"Departamento ignorado: {chave}")
                continue

            if isinstance(valor, dict):
                total += soma_recursiva(valor)

            elif isinstance(valor, (int, float)):
                total += valor

        return total

    total_final = soma_recursiva(estrutura)

    total_convertido = total_final * taxa_cambio

    print(f"\nTotal em USD: {total_final:,.2f}")
    print(f"Moeda destino: {moeda_destino}")
    print(f"Taxa de câmbio aplicada: {taxa_cambio}")

    return total_convertido


if __name__ == "__main__":
    moeda = "BRL"
    resultado = calcular_orcamento(
        empresa,
        "RH",
        "Marketing",
        moeda_destino=moeda,
        taxa_cambio=5.20
    )
    print(f"\nOrçamento total convertido: {resultado:,.2f} {moeda}")
