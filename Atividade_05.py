# Atividade_05
# ---------------------------------------------------------------------
# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua
# preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;
# ---------------------------------------------------------------------


print()  # Adiciona uma linha em branco
print('=' * 22)
print()  # Adiciona uma linha em branco
print("""Atividade_05""")
print()  # Adiciona uma linha em branco
print('=' * 22)

# Solicita ao usuário que digite uma frase, removendo espaços extras no início e
# no final (strip) e convertendo para letras maiúsculas (upper)
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras, separando pelos espaços (split)
palavras = frase.split()

# Junta as palavras sem espaços entre elas (join) para formar uma única string contínua
junto = ''.join(palavras)

# Inicializa uma string vazia para armazenar a versão invertida da frase
inverso = ''

# Loop que percorre a string 'junto' de trás para frente, construindo a string 'inverso'
for letra in range(len(junto) - 1, -1, -1):
    # Adiciona cada letra na string 'inverso'
    inverso += junto[letra]
# This line of code is using f-string formatting to create a formatted output. Here's a breakdown of
# what it does:
print(f'\nO inverso de \033[1;31;4m{junto}\033[m é -> \033[1;32;4m{inverso}\033[m\n')
