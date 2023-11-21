nome = 'Tony'
sobrenome = 'Stark'
nome_completo = nome + ' ' + sobrenome

print(nome)
print(sobrenome)
print(nome_completo)

congratulacao = 'Feliz'
situacao_1 = 'Natal.'
situacao_2 = 'Ano Novo.'

mensagem_1 = f"Tenha um {congratulacao} dia de {situacao_1}"
mensagem_2 = f"Tenha um {congratulacao} dia de {situacao_2}"

print(mensagem_1)
print(mensagem_2)

versao = 'ABC123'
print(versao)
versao += '-10' # versao = versao + '-10'
print(versao)

existe_feliz = 'Feliz' in mensagem_1
existe_infeliz = 'Infeliz' in mensagem_1
print(existe_feliz)
print(existe_infeliz)

print(mensagem_1[6])
print(mensagem_1[0:10])
print(mensagem_1[9:15])

print('Abc')
print('Abc'.lower())
print('Abc'.upper())

print('Abc'.find('b'))
print('Abc'.replace('b', 'x'))
