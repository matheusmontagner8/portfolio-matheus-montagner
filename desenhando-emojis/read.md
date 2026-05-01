# 🎨 Emoji Pixel Art: Processamento de Matrizes RGB

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de manipulação de imagens em baixo nível, utilizando estruturas de dados em Python para representar e transformar matrizes de pixels (Pixel Art). O objetivo principal é demonstrar como algoritmos de processamento de imagem podem alterar propriedades visuais, como brilho e tonalidade, diretamente nos canais de cor RGB.

O software processa um dicionário contendo o mapeamento de cores de um "Emoji", percorre sua grade de pixels e aplica uma transformação matemática para reduzir a intensidade cromática das cores primárias. O resultado final é renderizado visualmente, permitindo comparar a estrutura lógica dos dados com a saída gráfica.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Bibliotecas:** Matplotlib (para visualização de dados)
* **Conceitos:** Manipulação de Dicionários, Iteração de Matrizes (Nested Loops) e Processamento de Tuplas RGB.
* **Ferramentas:** Google Colab / Jupyter Notebook.

## 📊 Funcionamento do Algoritmo
O projeto opera através de um pipeline de transformação de dados:

1.  **Mapeamento:** Os dados são extraídos de uma estrutura `emoji_data` contendo o nome e a grade de cores (RGB).
2.  **Transformação (Filtro):** O algoritmo identifica pixels específicos (amarelo: `255, 255, 0`) e aplica uma divisão inteira (`// 2`) em cada canal de cor.
3.  **Reconstrução:** Uma nova grade é gerada e reinserida no dicionário original.
4.  **Visualização:** A biblioteca `Matplotlib` converte a matriz numérica em uma imagem visualizável.

## 📊 Resultados e Aprendizados
O desenvolvimento deste exercício proporcionou aprendizados práticos em computação gráfica básica:
*   **Acesso a Matrizes:** Aprendi a navegar em listas aninhadas para modificar elementos específicos sem alterar a estrutura global.
*   **Manipulação de Cores:** Compreendi como a alteração dos valores numéricos em tuplas RGB impacta diretamente na percepção visual de brilho e saturação.
*   **Renderização:** Implementei o uso de `plt.imshow()` para transformar dados brutos em representações gráficas claras.

## 🔧 Como Executar
1. Clone o repositório.
2. Instale a biblioteca necessária: 
   ```bash
   pip install matplotlib
