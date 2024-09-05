# -----------------------------------------------------------
# Estágio - São Paulo:
# -----------------------------------------------------------
# Atividade_02
# ---------------------------------------------------------------------
#  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na
# linguagem que desejar onde, informado um número, ele calcule a sequência
# de Fibonacci e retorne uma mensagem avisando se o número informado pertence
# ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua
# preferência ou pode ser previamente definido no código;
# ---------------------------------------------------------------------

# Imprime o título

print()  # Adiciona uma linha em branco
print('=' * 22)
print()  # Adiciona uma linha em branco
print("""Atividade_02""")
print()  # Adiciona uma linha em branco
print('=' * 22)

# Solicita ao usuário o número de termos a serem mostrados
n = int(input('\nQuantos termos você quer mostrar: '))

# Inicializa os dois primeiros termos da sequência de Fibonacci
t1 = 0
t2 = 1

# Imprime uma linha separadora
print('~' * 50)

# Exibe os dois primeiros termos da sequência
print(f'{t1} -> {t2}', end='')

# Inicia o contador a partir do terceiro termo
cont = 3

# Loop para calcular e mostrar a sequência de Fibonacci até o número de termos solicitado
while cont <= n:
    # Calcula o próximo termo na sequência
    t3 = t1 + t2

    # Imprime o próximo termo, mantendo a mesma linha
    print(f' -> {t3}', end='')

    # Atualiza os valores para o próximo ciclo
    t1 = t2
    t2 = t3
    cont += 1

# Imprime uma linha em branco para separar a sequência da próxima parte
print('\n')

# -----------------------------------------------------------
# Verificação de número na sequência de Fibonacci
# -----------------------------------------------------------

# Solicita ao usuário um número para verificar se pertence à sequência de Fibonacci
numero = int(
    input('\nDigite um número para verificar se pertence à sequência de Fibonacci: '))

# Reinicializa os primeiros números de Fibonacci
t1, t2 = 0, 1

# Variável para verificar se o número está na sequência
pertence = False

# Loop para calcular a sequência de Fibonacci até o número informado
while t1 <= numero:
    if t1 == numero:
        pertence = True
        break
    # Atualiza os valores para o próximo número na sequência
    t1, t2 = t2, t1 + t2

# Imprime o resultado
if pertence:
    # usei a formatação ANSI para exibir o texto em verde, negrito e sublinhado
    print(f'\nO número \033[1;32;4m{numero} PERTENCE\033[m à sequência de Fibonacci.\n')
else:
    # Usei a formatação ANSI para exibir o texto em vermelho, negrito e sublinhado
    print(f'\nO número \033[1;31;4m{numero} NÃO PERTENCE\033[m à sequência de Fibonacci.\n')

# Imprime o final da sequência
print('\nFim\n')
