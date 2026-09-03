# 💸 Sistema de Caixa e Decomposição de Troco

## 📝 Descrição do Projeto
Este projeto consiste em um algoritmo de automação para PDV (Ponto de Venda), focado na lógica de validação de pagamentos e cálculo otimizado de troco. O objetivo principal é garantir que a devolução de valores seja feita utilizando o menor número possível de cédulas, mitigando erros humanos e agilizando o atendimento.

O sistema processa o valor total da compra e o valor entregue pelo cliente, validando a suficiência do pagamento antes de prosseguir para a decomposição aritmética do troco em notas de R$ 100, 50, 10, 5 e 1.

![Fluxograma do Processo](1000151272.jpg)
*Figura 1: Fluxograma lógico da validação e cálculo de troco.*

## 🚀 Lógica de Funcionamento
O algoritmo foi estruturado seguindo as melhores práticas de lógica de programação, dividindo-se em quatro etapas principais:

1.  **Entrada e Validação:** Leitura dos valores de compra e pagamento, com verificação de "Valor Insuficiente".
2.  **Cálculo de Diferença:** Determinação do valor líquido a ser devolvido (`troco = pago - total`).
3.  **Decomposição Aritmética:** Utilização de operadores de divisão inteira (`Div`) e resto (`Mod`) para calcular a quantidade exata de cada cédula.
4.  **Saída de Dados:** Exibição detalhada das notas a serem devolvidas ao usuário.

## 📊 Estrutura Técnica
*   **Paradigma:** Lógica de Programação e Fluxogramação.
*   **Operadores Chave:** `Div` (quociente) e `Mod` (resto da divisão).Aqui está o README estruturado para o seu projeto de sistema de caixa e cálculo de troco, baseado no pseudocódigo e nos fluxogramas fornecidos:
```markdown
# 💸 Sistema de Caixa e Decomposição de Troco

## 📝 Descrição do Projeto
Este projeto consiste em um algoritmo de automação para PDV (Ponto de Venda), focado na lógica de validação de pagamentos e cálculo otimizado de troco. O objetivo principal é garantir que a devolução de valores seja feita utilizando o menor número possível de cédulas, mitigando erros humanos e agilizando o atendimento.

O sistema processa o valor total da compra e o valor entregue pelo cliente, validando a suficiência do pagamento antes de prosseguir para a decomposição aritmética do troco em notas de R$ 100, 50, 10, 5 e 1.

![Fluxograma do Processo](1000151272.jpg)
*Figura 1: Fluxograma lógico da validação e cálculo de troco.*

## 🚀 Lógica de Funcionamento
O algoritmo foi estruturado seguindo as melhores práticas de lógica de programação, dividindo-se em quatro etapas principais:

1.  **Entrada e Validação:** Leitura dos valores de compra e pagamento, com verificação de "Valor Insuficiente".
2.  **Cálculo de Diferença:** Determinação do valor líquido a ser devolvido (`troco = pago - total`).
3.  **Decomposição Aritmética:** Utilização de operadores de divisão inteira (`Div`) e resto (`Mod`) para calcular a quantidade exata de cada cédula.
4.  **Saída de Dados:** Exibição detalhada das notas a serem devolvidas ao usuário.

## 📊 Estrutura Técnica
*   **Paradigma:** Lógica de Programação e Fluxogramação.
*   **Operadores Chave:** `Div` (quociente) e `Mod` (resto da divisão).
*   **Cédulas Suportadas:** R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1.

## 🔧 Exemplo de Fluxo (Pseudocódigo)
O núcleo do sistema utiliza a seguinte lógica para decomposição:

```pascal
// Exemplo para notas de 100
nota100 <- resto Div 100
resto <- resto Mod 100
// Repete-se para as demais notas (50, 10, 5, 1)
