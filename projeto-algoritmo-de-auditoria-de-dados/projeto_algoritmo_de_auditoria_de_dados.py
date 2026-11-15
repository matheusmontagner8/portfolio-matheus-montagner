# -*- coding: utf-8 -*-
"""Algoritmo de Auditoria de Dados

Lê três vendas e o limite liberado pelo gerente, calcula a média
e classifica o resultado da auditoria.

Autor: Matheus Montagner
"""

LIMITE_SEGURANCA = 10.0


def ler_valor(mensagem):
    """Pede um número até o usuário digitar um valor válido."""
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("Valor inválido. Digite apenas números (ex.: 150.50).")
            continue

        if valor < 0:
            print("O valor não pode ser negativo.")
            continue

        return valor


def analisar_vendas():
    """Permite que o gerente altere o limite de segurança (variável global)."""
    global LIMITE_SEGURANCA
    LIMITE_SEGURANCA = ler_valor("Valor liberado pelo gerente: ")


def classificar(media):
    """Retorna o status da auditoria de acordo com o limite atual."""
    if media <= LIMITE_SEGURANCA:
        return "Limite Liberado"
    elif media > LIMITE_SEGURANCA * 5:
        return "Revisão Manual"
    else:
        return "Sistema em Quarentena"


def main():
    venda1 = ler_valor("Valor da primeira venda: ")
    venda2 = ler_valor("Valor da segunda venda: ")
    venda3 = ler_valor("Valor da terceira venda: ")

    media_final = (venda1 + venda2 + venda3) / 3

    analisar_vendas()

    # Saída
    print("-" * 40)
    print(f"Primeira venda: {venda1:.2f} | Tipo: {type(venda1)}")
    print(f"Segunda venda: {venda2:.2f} | Tipo: {type(venda2)}")
    print(f"Terceira venda: {venda3:.2f} | Tipo: {type(venda3)}")
    print(f"Média: {media_final:.2f} | Tipo: {type(media_final)}")
    print(f"Limite de segurança: {LIMITE_SEGURANCA:.2f}")
    print(f"Status: {classificar(media_final)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
