# 🚀 Desafios de Programação em Python - Estágio São Paulo

Este repositório contém cinco atividades práticas desenvolvidas em Python, propostas como parte de um processo seletivo de estágio. Cada exercício aborda conceitos essenciais como lógica de programação, automação de tarefas, manipulação de arquivos, estruturas de repetição e strings.

---

## 📂 Atividades

### 🧠 Atividade 01 – Automação de Cadastro com PyAutoGUI e Pandas

O sistema lê um arquivo CSV com dados de produtos e realiza cadastros automaticamente via automação no navegador.

**📝 Estrutura esperada do CSV:**
csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Nike,Tênis,Esporte,299.90,150,-
Automatiza login e entrada de dados

Utiliza pyautogui para simular ações do teclado e mouse

Manipula dados com pandas

## 🔢 Atividade 02 – Verificação de Número na Sequência de Fibonacci
Recebe um número e verifica se ele pertence à sequência de Fibonacci.

Utiliza estrutura while para gerar a sequência

Entrada e saída interativas no terminal

Uso de cores ANSI para melhor visualização

## 📊 Atividade 03 – Análise de Faturamento (JSON)
Lê um arquivo dados.json com valores diários de faturamento e exibe:

O menor e o maior faturamento

A média mensal

Quantos dias o faturamento foi acima da média

Inclui tratamento de erros e validações.

## 📈 Atividade 04 – Percentual por Estado
Calcula a participação percentual de cada estado no faturamento mensal total:

text
Copiar
Editar
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Resultado exibido com duas casas decimais

Ideal para aplicação prática em dashboards

## 🔄 Atividade 05 – Inversão de String
Recebe uma string digitada pelo usuário e exibe a versão invertida, sem utilizar funções prontas como reverse() ou slicing [::-1].

Aplicação de lógica com for e manipulação de índices

Uso de cores ANSI para destaque

## 📌 Como usar
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
Instale os pacotes necessários (caso deseje rodar a automação da Atividade 01):

bash
Copiar
Editar
pip install pyautogui pandas
Execute os arquivos Python individualmente:

bash
Copiar
Editar
python atividade_01.py
💻 Tecnologias utilizadas
Python 3.10+

Pandas

PyAutoGUI

JSON

ANSI Escape Sequences

## 📁 Estrutura do Projeto
pgsql
Copiar
Editar
├── atividade_01_automacao.py
├── atividade_02_fibonacci.py
├── atividade_03_faturamento_json.py
├── atividade_04_percentual_estado.py
├── atividade_05_inversao_string.py
├── dados.json
├── produtos.csv
└── README.md
