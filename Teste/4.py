# Define os dados de faturamento por estado
state_revenue = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
total_revenue = sum(state_revenue.values())

# Calcula a porcentagem de representação de cada estado
representation_percentage = {state: (revenue / total_revenue) * 100 for state, revenue in state_revenue.items()}

# Imprime a porcentagem de representação
for state, percentage in representation_percentage.items():
    print(f'{state}: {percentage:.2f}%')