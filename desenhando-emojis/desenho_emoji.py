# -*- coding: utf-8 -*-
"""Desenhando Emojis com Dados

1. Emoji 5x5 em RGB: escurece os pixels amarelos e mostra antes/depois.
2. Biblioteca musical: transpõe matrizes guardadas em tuplas.
3. Playlist de imagens: altera pixels e manipula a lista de imagens.

Autor: Matheus Montagner
"""

import copy

import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Emoji 5x5
# ---------------------------------------------------------------
emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],
        [(255,255,0), (0,0,0),     (255,255,0), (0,0,0),     (255,255,0)],
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],
        [(255,255,0), (0,0,0),     (0,0,0),     (0,0,0),     (255,255,0)],
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)]
    ]
}

# Guarda uma cópia da grade original para comparar no final
grade_original = copy.deepcopy(emoji_data["grade"])

nova_grade = []

for chave, valor in emoji_data.items():
    if chave == "grade":
        for linha in valor:
            nova_linha = []
            for pixel in linha:

                # Pixel amarelo: divide cada canal por 2 (fica mais escuro)
                if pixel == (255, 255, 0):
                    r, g, b = pixel
                    novo_pixel = (r // 2, g // 2, b // 2)
                    nova_linha.append(novo_pixel)
                else:
                    nova_linha.append(pixel)

            nova_grade.append(nova_linha)

emoji_data["grade"] = nova_grade

for linha in emoji_data["grade"]:
    print(linha)

# ---------------------------------------------------------------
# 2. Biblioteca musical: transposição de matrizes
# ---------------------------------------------------------------
biblioteca_musical = {
    "Toques": [
        {"Alegre": ([440, 480], [520, 560])},
        {"Triste": ([200, 150], [100, 50])}
    ]
}

for item in biblioteca_musical["Toques"]:
    for nome, matriz in item.items():

        nova_matriz = []
        linhas = list(matriz)

        # Linhas viram colunas
        for i in range(len(linhas[0])):
            nova_linha = []
            for j in range(len(linhas)):
                nova_linha.append(linhas[j][i])
            nova_matriz.append(nova_linha)

        item.update({nome: nova_matriz})

for item in biblioteca_musical["Toques"]:
    print(item)

# ---------------------------------------------------------------
# 3. Playlist de imagens
# ---------------------------------------------------------------
playlist = {
    "nome": "Mix Emoji",
    "imagens": [
        {
            "titulo": "Sol",
            "pixels": [
                [(255,255,0), (255,255,0)],
                [(255,255,0), (0,0,0)]
            ]
        },
        {
            "titulo": "Noite",
            "pixels": [
                [(0,0,0), (255,255,0)],
                [(255,255,0), (255,255,0)]
            ]
        }
    ]
}

for chave in playlist.keys():
    if chave == "imagens":
        for imagem in playlist[chave]:
            for linha in imagem["pixels"]:
                for i in range(len(linha)):
                    pixel = linha[i]

                    if pixel == (255,255,0):
                        r, g, b = pixel
                        linha[i] = (r//2, g//2, b//2)

# Insere uma imagem no início e remove a última
playlist["imagens"].insert(0, {
    "titulo": "Novo",
    "pixels": [[(0,0,0)]]
})
playlist["imagens"].pop()

for img in playlist["imagens"]:
    print(img["titulo"], img["pixels"])

# ---------------------------------------------------------------
# Visualização: emoji antes e depois do filtro
# ---------------------------------------------------------------
fig, (antes, depois) = plt.subplots(1, 2, figsize=(6, 3))

antes.imshow(grade_original)
antes.set_title("Original")
antes.axis("off")

depois.imshow(emoji_data["grade"])
depois.set_title("Amarelo escurecido")
depois.axis("off")

plt.show()
