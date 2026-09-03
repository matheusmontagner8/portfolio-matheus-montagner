
 
📝 Descrição do Projeto
Este projeto consiste em um script de auditoria automatizada desenvolvido em Python para monitorar o volume de vendas e garantir a conformidade com diretrizes de segurança financeira. O sistema calcula a média de transações recentes e a compara com um limite dinâmico (definido pelo nível gerencial) para determinar se a operação deve ser liberada ou bloqueada.

O algoritmo classifica as operações em quatro estados críticos:

Limite Liberado: A média está dentro dos parâmetros de segurança.

Sistema em Quarentena: A média excedeu levemente o limite permitido.

Revisão Manual: Detectado um desvio de segurança gravíssimo (5x acima do limite).

Valor não identificado: Tratamento de exceções de dados.

🚀 Tecnologias Utilizadas
Linguagem: Python 3.x

Conceitos Aplicados: Manipulação de tipos (float), funções com escopo global, estruturas condicionais compostas e entrada de dados dinâmica.

Ferramentas: Google Colab / Jupyter Notebook.

📊 Funcionamento do Algoritmo
O fluxo de execução segue uma lógica de pipeline de dados simples e eficaz:

Entrada: O usuário insere os valores de três vendas consecutivas.

Processamento: O sistema calcula a média aritmética simples das vendas.

Intervenção: A função analisar_vendas() permite que um gestor atualize o LIMITE_SEGURANCA em tempo real usando a diretiva global.

Saída: Um relatório detalhado exibindo os valores, os tipos de dados processados e o status final da auditoria.

🔧 Como Executar
Certifique-se de ter o Python instalado ou utilize o Google Colab.

Clone o repositório ou baixe o arquivo .ipynb.

Execute a célula principal.

Insira os valores solicitados no terminal:

Valor da venda 1, 2 e 3.

Valor liberado pelo gerente (Limite).

O sistema imprimirá o relatório de auditoria automaticamente.
