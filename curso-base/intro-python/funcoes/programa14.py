def calcular_idade(ano_nascimento, ano_atual=2023):
    idade = ano_atual - ano_nascimento
    return idade
    print(idade)

resultado = calcular_idade(1998)
print(f'Sua idade é {resultado}.')

def calcular_bioimpedancia(massa_kg, altura_m):
    imc = massa_kg / (altura_m ** 2)
    total_massa_gorda = massa_kg * 29 / 100
    return imc, total_massa_gorda

imc_calculado, massa_gorda = calcular_bioimpedancia(78, 1.75)
print(f'''Seu IMC é {imc_calculado} kg/m² e 
seu total de gordura é {massa_gorda} kg.''')
