import json

# Carregar os dados do faturamento a partir do arquivo JSON
with open("3/faturamento.json", "r") as file:
    data = json.load(file)

faturamento = data["faturamento"]

# Remover dias sem faturamento (zero)
faturamento_filtrado = [valor for valor in faturamento if valor > 0]

# Calcular o menor e o maior faturamento diário
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

# Calcular a média mensal considerando apenas os dias com faturamento
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Contar os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

# Exibir os resultados
print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
