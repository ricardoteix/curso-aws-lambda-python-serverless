# gato = dict(nome='Obi-Wan', idade=2)
gato = { 
    'nome': 'Obi-Wan', 
    'idade': 2 
}

print(type(gato))
print(gato)

carro_1 = {
    'cor': 'cinza',
    'ano': 2008,
    'modelo': 'Gol',
    'marca': 'VW',
    'ipva': True
}
print(carro_1)

print(carro_1['ano'])
print(carro_1['marca'])
print(carro_1['modelo'])
print('tanque' in carro_1)
print(len(carro_1))

del carro_1['marca']
# print(carro_1['marca'])
print(len(carro_1))
print(list(carro_1))

carro_1['ano'] = 2007
print(carro_1['ano'])

