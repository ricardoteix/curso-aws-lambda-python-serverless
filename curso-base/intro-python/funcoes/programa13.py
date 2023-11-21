def calcular_idade(ano_nascimento, ano_atual=2023):
    idade = ano_atual - ano_nascimento
    print(f'Você completou {idade} anos em {ano_atual}.')

# calcular_idade(1985, 2023)
# calcular_idade(2000, 2023)
# calcular_idade(1960, 2023)

calcular_idade(1985)
calcular_idade(2000, 2020)
calcular_idade(1960)
calcular_idade(ano_atual=2022, ano_nascimento=1980)
