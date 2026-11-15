# Orçamento Corporativo com Recursão (Python)

Exercício da disciplina de Programação de Computadores (Análise e Desenvolvimento de Sistemas, Unicid).

## O que o programa faz

A estrutura de uma empresa fictícia fica guardada em **dicionários aninhados** (unidade → setor → área → orçamento em USD):

```python
empresa = {
    "Matriz": {
        "TI": {"Infraestrutura": 50000, "Desenvolvimento": 80000, "Seguranca": 30000},
        "RH": {"Recrutamento": 20000, "Treinamento": 15000},
        ...
    },
    "Filial": { ... }
}
```

A função `calcular_orcamento()`:

- soma todos os valores, em qualquer nível de profundidade;
- ignora os setores informados (ex.: `"RH"`, `"Marketing"`), incluindo todas as áreas abaixo deles;
- converte o total para outra moeda, se uma taxa de câmbio for informada.

O decorator `@auditor` envolve a função e mostra quais setores foram ignorados, os parâmetros extras e o tempo de execução. Para isso, ele não precisa alterar o cálculo.

## Conceitos praticados

- **Recursão:** `soma_recursiva()` chama a si mesma sempre que encontra outro dicionário.
- **Decorators:** `@auditor` adiciona registro e cronometragem.
- **`*args` e `**kwargs`:** setores ignorados e opções de câmbio são passados em quantidade variável.

## Como executar

```bash
python sistema_de_auditoria.py
```

## Exemplo de saída

```
=============================================
INICIANDO AUDITORIA FINANCEIRA
Função auditada: calcular_orcamento
Setores ignorados: RH, Marketing
Parâmetros extras: {'moeda_destino': 'BRL', 'taxa_cambio': 5.2}
Departamento ignorado: RH
Departamento ignorado: Marketing

Total em USD: 225,000.00
Moeda destino: BRL
Taxa de câmbio aplicada: 5.2
Tempo de execução: 0.048 ms
AUDITORIA CONCLUÍDA
=============================================

Orçamento total convertido: 1,170,000.00 BRL
```

[⬅ Voltar ao portfólio](../)
