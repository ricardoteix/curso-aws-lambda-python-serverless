datas = [3, 14, 9, 22, 8]
animais = ["gato", "cachorro", "coelho", "baleia","porg"]
dados = {
    'nome': 'Luke',
    'email': 'luke@gmail.com',
    'nascimento': 1977
}

for animal in animais:
    print(f'Eu tenho um {animal}.')

for chave in dados:
    print(f'O valor do {chave} é {dados[chave]} ')

for numero in range(10, 21):
    print(numero)

print('-----')
print(datas)

for indice, data in enumerate(datas):
    datas[indice] = data * 2
    print(f'indice {indice} data {datas[indice]}')

print(datas)