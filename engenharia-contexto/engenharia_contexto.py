# -*- coding: utf-8 -*-
"""Engenharia de Contexto e Lógica Física

1. analisar(): qualidade do ar e nota de conforto em locais visitados.
2. simulador(): jogo de texto de evacuação de uma casa.

Autor: Matheus Montagner
"""


def analisar():
    dados = [
        # [Local, Temperatura, Umidade, IQA]

        ["Praça da Toco - manhã", 24, 60, 45],
        ["Praça da Toco - tarde", 28, 55, 60],

        ["Estação Vila Matilde - manhã", 24, 58, 95],
        ["Estação Vila Matilde - tarde", 30, 50, 120],

        ["Unicid - manhã", 25, 65, 80],
        ["Unicid - tarde", 31, 45, 120]
    ]

    for local in dados:
        print("\nLocal:", local[0])

        nomes = ["Temperatura", "Umidade", "IQA"]
        for i in range(1, 4):
            print(nomes[i-1], ":", local[i])

        temp = local[1]
        umidade = local[2]
        iqa = local[3]

        match iqa:
            case _ if iqa <= 50:
                qualidade = "Boa"
            case _ if iqa <= 100:
                qualidade = "Moderada"
            case _ if iqa <= 150:
                qualidade = "Ruim"
            case _:
                qualidade = "Muito ruim"

        nota = 10 - abs(temp - 24) - (iqa / 50)

        if nota < 0:
            nota = 0

        print("Qualidade do ar:", qualidade)
        print(f"Nota de conforto: {nota:.1f}")


def simulador():
    locais = ["Quarto", "Corredor", "Sala", "Outro corredor", "Porta de saída", "Rua"]
    estados = ["chave", "caminho livre", "fogo", "porta trancada", "saida"]

    posicao = 0
    energia = 10
    tem_chave = False

    print("=== SIMULADOR DE EVACUAÇÃO ===\n")

    while energia > 0:
        print("\nVocê está em:", locais[posicao])
        print("Situação:", estados[posicao])

        estado = estados[posicao]

        # ESCOLHA DO USUÁRIO (aceita "avançar" com ou sem cedilha)
        acao = input("O que deseja fazer? (avancar / voltar / verificar): ").lower().replace("ç", "c")

        if acao == "verificar":
            print("Energia:", energia)
            print("Tem chave?", tem_chave)

        elif acao == "avancar":

            if estado == "chave":
                print("Você encontrou uma chave!")
                tem_chave = True
                posicao += 1

            elif estado == "caminho livre":
                print("Caminho livre, você avançou.")
                posicao += 1

            elif estado == "fogo":
                print("Tem fogo aqui!")

                # IF aninhado
                if energia > 2:
                    escolha = input("Quer tentar atravessar? (sim/nao): ").lower()

                    if escolha == "sim":
                        print("Você atravessou o fogo!")
                        energia -= 2
                        posicao += 1
                    else:
                        print("Você decidiu voltar.")
                        posicao -= 1
                else:
                    print("Você não tem energia suficiente!")
                    posicao -= 1

            elif estado == "porta trancada":
                print("A porta está trancada!")

                # IF aninhado (inventário)
                if tem_chave:
                    usar = input("Deseja usar a chave? (sim/nao): ").lower()

                    if usar == "sim":
                        print("Porta aberta!")
                        posicao += 1
                    else:
                        print("Você decidiu não usar a chave.")
                else:
                    print("Você não tem chave!")
                    posicao -= 1

            elif estado == "saida":
                print("Você saiu da casa! Parabéns 🚀")
                break

        elif acao == "voltar":
            if posicao > 0:
                posicao -= 1
                print("Você voltou um passo.")
            else:
                print("Você já está no início.")

        else:
            print("Ação inválida!")

        energia -= 1
        print("Energia restante:", energia)
        print("-" * 30)

    if energia <= 0:
        print("\nVocê ficou sem energia... não conseguiu sair.")


if __name__ == "__main__":
    analisar()
    simulador()
