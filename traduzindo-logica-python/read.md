# 🛡️ Algoritmo de Auditoria e Segurança de Transações

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de auditoria automatizada desenvolvido para monitorar fluxos de vendas e garantir a conformidade com diretrizes de segurança financeira. O algoritmo atua como uma camada de controle, processando transações recentes e validando-as contra limites dinâmicos estabelecidos pela gestão.

O objetivo principal é identificar desvios operacionais e classificar o status do sistema em tempo real, permitindo a interrupção de fluxos suspeitos e a mitigação de riscos financeiros através de estados de "Quarentena" ou "Revisão Manual".



## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Conceitos Aplicados:** Manipulação de tipos primitivos (float), escopo global de variáveis, estruturas condicionais compostas e lógica de tomada de decisão.
* **Ferramentas:** Google Colab, Jupyter Notebook.

## 📊 Regras de Negócio e Estados do Sistema
O algoritmo avalia a média aritmética de vendas consecutivas e aplica a seguinte lógica de auditoria:

* **Liberação Padrão:** Média de vendas dentro do limite de segurança definido.
* **Sistema em Quarentena:** Ativado quando a média excede o limite permitido, sinalizando necessidade de atenção.
* **Revisão Manual (Crítica):** Ativada quando a média excede em 5x o limite de segurança, bloqueando processos para inspeção humana.



## 📊 Resultados e Aprendizados
O desenvolvimento deste script permitiu o aprofundamento em técnicas de controle de fluxo e integridade de dados:
* **Escopo Dinâmico:** Implementação de funções que permitem a atualização do limite de segurança em tempo de execução via input gerencial.
* **Tratamento de Dados:** Validação de inputs numéricos para garantir a precisão dos cálculos de média final.
* **Classificação de Status:** Desenvolvimento de uma matriz de decisão para categorizar a saúde da operação financeira.

## 🔧 Como Executar
1. Acesse o projeto via **Google Colab** ou clone o repositório.
2. Execute o script principal.
3. Insira os valores das vendas solicitados pelo terminal.
4. Defina o limite de segurança conforme orientado pelo sistema.
5. Visualize o relatório final com a média das vendas, o status da auditoria e o tipo de dado processado.

---
**Desenvolvido como projeto prático de Lógica de Programação e Auditoria de Dados.**

