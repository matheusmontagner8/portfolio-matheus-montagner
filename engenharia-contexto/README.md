# 🌍 Monitoramento Ambiental: Qualidade do Ar e Conforto

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de análise de dados ambientais focado no monitoramento da qualidade do ar (IQA) e no cálculo de índices de conforto térmico em diferentes localidades urbanas. O objetivo principal é fornecer uma visão clara sobre as condições atmosféricas e o bem-estar dos cidadãos em pontos estratégicos da cidade.

O sistema processa variáveis como temperatura, umidade e o Índice de Qualidade do Ar (IQA) para classificar o ambiente e gerar uma "Nota de Conforto" personalizada. Essa nota é calculada através de um algoritmo que penaliza desvios da temperatura ideal e altos níveis de poluição, facilitando a tomada de decisão para atividades ao ar livre.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Conceitos:** Estruturas de repetição, lógica de decisão condicional (`match-case`), manipulação de listas e algoritmos matemáticos de normalização.
* **Ferramentas:** VS Code, Google Colab ou qualquer interpretador Python 3.x.

## 📊 Regras de Negócio e Cálculos
O algoritmo utiliza métricas específicas para avaliar o ambiente em pontos como a Praça da Toco, Estação Vila Matilde e Unicid:

1.  **Classificação do IQA:**
    *   **Boa:** IQA <= 50.
    *   **Moderada:** IQA entre 51 e 100.
    *   **Ruim:** IQA entre 101 e 150.
    *   **Muito Ruim:** IQA > 150.
2.  **Nota de Conforto:**
    *   Calculada com base na proximidade da temperatura de referência (24°C) e no impacto negativo da poluição do ar.

## 📊 Resultados e Aprendizados
Durante o desenvolvimento deste projeto, foram aplicadas técnicas fundamentais de engenharia de software:
*   **Processamento de Dados Multidimensionais:** Organização de dados geolocalizados em listas para iteração eficiente.
*   **Lógica de Classificação:** Implementação do `match-case` para categorização precisa de índices de poluição.
*   **Modelagem de Índices:** Criação de uma fórmula de conforto térmico que equilibra variáveis ambientais distintas.

## 🔧 Como Executar
1. Clone o repositório ou copie o código fonte.
2. Certifique-se de ter o Python 3.x instalado em sua máquina.
3. Execute o script principal:
   ```bash
   python main.py
