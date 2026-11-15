# Auditoria de Vendas (Python)

Exercício da disciplina de Programação de Computadores (Análise e Desenvolvimento de Sistemas, Unicid).

## O que o programa faz

1. Lê o valor de três vendas.
2. Calcula a média.
3. Pede ao gerente o novo limite de segurança. A função `analisar_vendas()` altera a variável global `LIMITE_SEGURANCA`.
4. Mostra os valores, o tipo de cada dado e o status da auditoria:

| Status | Quando acontece |
| --- | --- |
| Limite Liberado | média menor ou igual ao limite |
| Sistema em Quarentena | média acima do limite |
| Revisão Manual | média mais de 5 vezes acima do limite |

Se o usuário digitar texto ou um número negativo, o programa avisa e pede o valor de novo, sem encerrar com erro. A vírgula também é aceita como separador decimal (ex.: `150,50`).

## Conceitos praticados

- Conversão de tipos com `float()` e exibição com `type()`
- Variável global alterada dentro de função (`global`)
- Condicionais com `if / elif / else`
- Tratamento de erro com `try / except ValueError`

## Como executar

Com o Python 3 instalado:

```bash
python projeto_algoritmo_de_auditoria_de_dados.py
```

Ou copie o código para uma célula do [Google Colab](https://colab.research.google.com/) e execute.

## Exemplo de saída

```
Valor da primeira venda: abc
Valor inválido. Digite apenas números (ex.: 150.50).
Valor da primeira venda: 100
Valor da segunda venda: 200,5
Valor da terceira venda: 300
Valor liberado pelo gerente: 50
----------------------------------------
Primeira venda: 100.00 | Tipo: <class 'float'>
Segunda venda: 200.50 | Tipo: <class 'float'>
Terceira venda: 300.00 | Tipo: <class 'float'>
Média: 200.17 | Tipo: <class 'float'>
Limite de segurança: 50.00
Status: Sistema em Quarentena
----------------------------------------
```

[⬅ Voltar ao portfólio](../)
