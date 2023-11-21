import json

dados = """
    {
        "nome": "Nome da Pessoa",
        "endereco": "Rua Tal, n 76",
        "cpf": "123.345.987-90",
        "casado": true,
        "imoveis": [
            "casa", "sítio"
        ],
        "idade": 65
    }
"""

pessoa = json.loads(dados)

print(dados)
print(pessoa)
print(type(dados))
print(type(pessoa))
print(pessoa['nome'], pessoa['endereco'])
print('-------')

info = { 
    'qtd_ec2': 5, 
    'type_ec2': 't3a.micro', 
    'ligado': True 
}
info_json = json.dumps(info)
print(info)
print(info_json)
print(type(info))
print(type(info_json))