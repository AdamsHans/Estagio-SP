# -----------------------------------------------------------
# Estágio - São Paulo:
# -----------------------------------------------------------
# Atividade_04
# ---------------------------------------------------------------------
# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação
# que cada estado teve dentro do valor total mensal da distribuidora.
# ---------------------------------------------------------------------

print()  # Adiciona uma linha em branco
print('=' * 22)
print()  # Adiciona uma linha em branco
print("""Atividade_04""")
print()  # Adiciona uma linha em branco
print('=' * 22)

# Valores de faturamento por estado
faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_Outros = 19849.53

# Calcula o faturamento total
faturamento_total = (faturamento_SP + faturamento_RJ +
                     faturamento_MG + faturamento_ES +
                     faturamento_Outros)

# Calcula o percentual de cada estado
percentual_SP = (faturamento_SP / faturamento_total) * 100
percentual_RJ = (faturamento_RJ / faturamento_total) * 100
percentual_MG = (faturamento_MG / faturamento_total) * 100
percentual_ES = (faturamento_ES / faturamento_total) * 100
percentual_Outros = (faturamento_Outros / faturamento_total) * 100

# Exibe os resultados
print(f'\nSP: {percentual_SP:.2f}%')
print(f'RJ: {percentual_RJ:.2f}%')
print(f'MG: {percentual_MG:.2f}%')
print(f'ES: {percentual_ES:.2f}%')
print(f'Outros: {percentual_Outros:.2f}%\n')
