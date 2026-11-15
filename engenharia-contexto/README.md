# Qualidade do Ar e Simulador de Evacuação (Python)

Exercício da disciplina de Programação de Computadores (Análise e Desenvolvimento de Sistemas, Unicid). Tem duas partes.

## 1. Qualidade do ar e nota de conforto: `analisar()`

Foram coletados manualmente dados de temperatura, umidade e IQA (Índice de Qualidade do Ar) em três locais, de manhã e à tarde: Praça da Toco, Estação Vila Matilde e Unicid.

Para cada medição, o programa:

- classifica o ar com `match-case`:

| IQA | Qualidade |
| --- | --- |
| até 50 | Boa |
| 51 a 100 | Moderada |
| 101 a 150 | Ruim |
| acima de 150 | Muito ruim |

- calcula uma **nota de conforto** de 0 a 10, que perde pontos quanto mais a temperatura se afasta de 24 °C e quanto maior o IQA:

```python
nota = 10 - abs(temp - 24) - (iqa / 50)
```

## 2. Simulador de evacuação: `simulador()`

Jogo de texto: o jogador precisa sair de casa antes de acabar a energia. Pelo caminho há uma chave, fogo e uma porta trancada. Cada ação gasta energia, e atravessar o fogo gasta mais.

## Conceitos praticados

- Listas e listas de listas
- `match-case` com condições (`case _ if ...`)
- Laço `while` com `break`
- `if` aninhado e variáveis de estado (energia, posição, inventário)

## Como executar

```bash
python engenharia_contexto.py
```

Primeiro aparece a análise do ar e depois começa o simulador. No simulador, digite `avancar`, `voltar` ou `verificar`.

## Exemplo de saída

```
Local: Praça da Toco - manhã
Temperatura : 24
Umidade : 60
IQA : 45
Qualidade do ar: Boa
Nota de conforto: 9.1
```

[⬅ Voltar ao portfólio](../)
