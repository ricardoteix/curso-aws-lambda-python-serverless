ec2_ids = []
print(type(ec2_ids))

datas = [3, 14, 9, 22, 8]
premios = [120.5, 99.2, 12.7]
mamiferos = [
    "gato",
    "cachorro", 
    "coelho"
]
aves = ["pardal", "tucano", "arara"]
dados = ["Anakin", 79, True]

"""

print(ec2_ids)
print(datas)
print(premios)
print(mamiferos)
print(aves)
print(dados)
"""

animais = [mamiferos, aves]
print(animais)

print(datas[0])
print(datas[4])

partes_data = datas[1:4]
print(partes_data)
print(partes_data[0])
print(partes_data[-1])

print(animais[0][1])
print(animais[1][1])

print('cachorro' in mamiferos)
print('jacare' in mamiferos)

print('jacare' not in mamiferos)
print([2, 4, 6] + [9, 8, 7])
print(len(mamiferos)) # 3
print(max(datas)) # 22
print(min(datas)) # 3

datas.append(31)
datas.append(1)
print(datas)

del datas[2]
print(datas)

datas.clear()
print(datas)