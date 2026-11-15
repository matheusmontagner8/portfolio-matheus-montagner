# Pixel Art com Matrizes RGB (Python)

Exercício da disciplina de Programação de Computadores (Análise e Desenvolvimento de Sistemas, Unicid).

## O que o programa faz

1. **Emoji 5x5:** um rosto sorridente é guardado como uma grade de cores RGB dentro de um dicionário. O programa percorre a grade, divide por 2 cada canal dos pixels amarelos (`(255, 255, 0)` vira `(127, 127, 0)`) e mostra o emoji **antes e depois** com o Matplotlib.
2. **Biblioteca musical:** transpõe matrizes guardadas em tuplas, ou seja, as linhas viram colunas.
3. **Playlist de imagens:** aplica o mesmo filtro em várias imagens e usa `insert()` e `pop()` para mexer na lista.

## Resultado

| Original | Amarelo escurecido |
| --- | --- |
| 🟨 amarelo `(255, 255, 0)` | 🟫 amarelo-escuro `(127, 127, 0)` |

## Conceitos praticados

- Dicionários, listas e tuplas
- Laços aninhados para percorrer matrizes
- Desempacotamento de tuplas (`r, g, b = pixel`) e divisão inteira (`//`)
- Visualização de dados com `plt.imshow()`

## Como executar

```bash
pip install matplotlib
python desenho_emoji.py
```

Ou execute no [Google Colab](https://colab.research.google.com/), que já tem o Matplotlib instalado.

[⬅ Voltar ao portfólio](../)
