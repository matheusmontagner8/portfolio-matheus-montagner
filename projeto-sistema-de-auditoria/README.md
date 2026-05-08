# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de [Nome da Disciplina] do curso de [Nome do Curso]. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   [(https://github.com/matheusmontagner8/portfolio-matheus-montagner)]
   ```
2. Acesse a pasta do projeto:
   ```bash
   [cd seu-repositorio](https://github.com/matheusmontagner8/portfolio-matheus-montagner/tree/main/projeto-sistema-de-auditoria)
   ```
3. Execute o script principal:
   ```bash
   [(https://colab.research.google.com/drive/1vE9C6jfPbNGmW1Kz61EG6M7jFNO5Yg_A?usp=sharing)]
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
Para percorrer toda essa estrutura sem precisar saber quantos níveis existem, foi utilizada uma função recursiva chamada soma_recursiva. Sempre que a função encontra um dicionário, ela chama a si mesma novamente para continuar navegando pelos níveis internos. Quando encontra um número, o valor é somado ao total do orçamento.

O decorator foi criado para adicionar funcionalidades extras sem que houvesse uma mudança que afetasse diretamente a função principal de cálculo. Ele foi acoplado antes da função calcular_orcamento. 
* **Dados:** Os dados simulados da empresa foram estruturados em... `[explique a estrutura do seu dicionário]`.
 
## 👤 Autor
 
* **Matheus Montagner** * LinkedIn: [(https://www.linkedin.com/in/matheus-montagner-97ba8b214/)]
* E-mail: [matheusmontagner8@gmail.com]
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
