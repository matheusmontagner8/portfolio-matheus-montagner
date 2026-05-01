# 🛡️ Sistema de Auditoria de Vendas e Fluxo de Triagem (Saúde Pública)

## 📝 Descrição do Projeto
Este repositório contém o desenvolvimento de um algoritmo de auditoria de dados financeiros e a modelagem lógica de um sistema de triagem para unidades de saúde. O projeto une a precisão da programação em **Python** com a estruturação de processos decisórios complexos (fluxogramas).

O motor de auditoria processa volumes de vendas, calcula médias e aplica regras de segurança dinâmicas para mitigar riscos operacionais e identificar anomalias, como sistemas em "quarentena" ou necessidade de "revisão manual". Paralelamente, o projeto documenta o pipeline de atendimento ao paciente, desde a triagem inicial baseada em sinais vitais até o diagnóstico e alta.

> **Status do Projeto:** Desenvolvido como parte de estudos em lógica de programação e arquitetura de sistemas (2024).

---

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Ambiente de Desenvolvimento:** Google Colab / Jupyter Notebook
* **Paradigma:** Programação Estruturada e Lógica Booleana
* **Documentação Técnica:** Fluxogramas de processos (saúde pública)

---

## 📊 Funcionalidades e Regras de Negócio

### 💰 Algoritmo de Auditoria
O sistema avalia a média de três vendas consecutivas contra um limite de segurança variável:
* **Limite Liberado:** Média dentro do teto estipulado pelo gerente.
* **Sistema em Quarentena:** Média superior ao limite de segurança.
* **Revisão Manual:** Média 5x superior ao limite (alerta de risco crítico).

### 🏥 Fluxo de Triagem (Sinais Vitais)
Baseado nos documentos anexos, o sistema de triagem segue a lógica:
1.  **Entrada:** Verificação de Febre, Pressão, Frequência Cardíaca e outros sinais graves.
2.  **Decisão:** Casos graves recebem atendimento imediato e possível internação. Casos não graves seguem para fila de espera e consulta de rotina.

---

## 📊 Resultados e Aprendizados
O projeto demonstrou eficácia na automação de verificações que antes seriam manuais:
* **Validação de Dados:** Implementação de conversão para `float` e tratamento de tipos primitivos para cálculos precisos.
* **Escopo Global:** Uso da instrução `global` em Python para permitir que funções de gerência alterem constantes do sistema em tempo de execução.
* **Modelagem de Processos:** Tradução de necessidades do mundo real (triagem hospitalar) em algoritmos lógicos e visuais.

---

## 🔧 Como Executar

1.  **Pré-requisitos:** Ter o Python 3.10 instalado ou uma conta no Google Colab.
2.  **Execução:**
    * Abra o arquivo `projeto-algoritmo-de-auditoria-de-dados.ipynb`.
    * Execute a célula principal.
    * Insira os valores das vendas e o limite de segurança conforme solicitado pelo prompt.
3.  **Interação:** O sistema retornará o status da auditoria e o relatório de tipos de dados processados.

---

## 📁 Estrutura de Arquivos
* `projeto-algoritmo-de-auditoria-de-dados.ipynb`: Código-fonte com a lógica de auditoria.
* `Fluxograma_Saude_Publica.jpg`: Representação visual do fluxo de triagem e atendimento.

---
[Voltar ao início](https://github.com/seu-usuario)
