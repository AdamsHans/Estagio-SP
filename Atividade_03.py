# -----------------------------------------------------------
# Estágio - São Paulo:
# -----------------------------------------------------------
# Atividade_03
# ---------------------------------------------------------------------
# Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?
# ---------------------------------------------------------------------

import json

print()  # Adiciona uma linha em branco
print('=' * 22)
print()  # Adiciona uma linha em branco
print("""Atividade_03""")
print()  # Adiciona uma linha em branco
print('=' * 22)

# Lista com o caminho completo do arquivo JSON
arquivos_json = [r'dados.json'
                 ]

# Itera sobre cada arquivo JSON na lista
for nome_arquivo in arquivos_json:
    try:
        # Carrega os dados do arquivo JSON
        with open(nome_arquivo, 'r') as file:
            dados = json.load(file)

        # Verifica se o conteúdo é uma lista
        if isinstance(dados, list):
            # Extrai os valores de faturamento, ignorando dias com valor 0 (sem faturamento)
            faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

            # Verifica se há dados de faturamento
            if not faturamentos:
                print(f"Não há dados de faturamento para processar em {nome_arquivo}.")
            else:
                # Calcula o menor e maior valor de faturamento
                menor_faturamento = min(faturamentos)
                maior_faturamento = max(faturamentos)

                # Calcula a média mensal
                media_mensal = sum(faturamentos) / len(faturamentos)

                # Conta o número de dias com faturamento acima da média
                dias_acima_media = sum(
                    1 for valor in faturamentos if valor > media_mensal)

                # Imprime os resultados
                print(f"\nMenor faturamento: {menor_faturamento:.2f}")
                print(f"Maior faturamento: {maior_faturamento:.2f}")
                print(f"Número de dias acima da média: {dias_acima_media}\n")

        else:
            print(f"O formato dos dados no arquivo {nome_arquivo} não é uma lista válida.")

    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON: {nome_arquivo}.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}\n")
