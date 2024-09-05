# -----------------------------------------------------------
# Estágio - São Paulo:
# -----------------------------------------------------------
# Atividade_01
# ---------------------------------------------------------------------
# Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?
# ---------------------------------------------------------------------

print()  # Adiciona uma linha em branco
print('=' * 22)
print()  # Adiciona uma linha em branco
print("""Atividade_01""")
print()  # Adiciona uma linha em branco
print('=' * 22)

# Solicita ao usuário o valor de INDICE
indice = int(
    input("\nDigite o número máximo até o qual deseja calcular a soma:  "))

# As Variáveis
soma = 0
k = 0

# Acumular a soma de 1 até o valor de INDICE
while k < indice:
    k += 1         # Incrementa o valor de K em 1
    soma += k      # Adiciona o valor de K à soma

# Imprime o resultado
print(f"\nO Valor Final da SOMA é: \033[1;35;4m{soma}\033[m\n")
