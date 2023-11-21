def calcular_idade(ano_nascimento, ano_atual=2023):
    idade = ano_atual - ano_nascimento
    return idade

def calcular_bioimpedancia(massa_kg, altura_m):
    imc = massa_kg / (altura_m ** 2)
    total_massa_gorda = massa_kg * 29 / 100
    return imc, total_massa_gorda
    
def enviar_email(destinatario, titulo, mensagem):
    remetente = "naoresponda@empresa.com.br"
    print(
        f"""Email enviado de {remetente} para {destinatario}.
        {titulo}
        {mensagem}"""
    )

usuario = {
    'nome': 'Tony Stark',
    'nascimento': 1960,
    'email': 'tonystark@gmail.com' 
}

idade = calcular_idade(usuario['nascimento'])
imc, massa_gorda = calcular_bioimpedancia(79, 1.8)
imc = round(imc) # arredonda o valor para inteiro
print(imc, massa_gorda, idade)

if imc <= 24 and idade <= 65:
    enviar_email(
        usuario['email'], 
        'EMC Bom', 
        f"Seu IMC está bom. Valor: {imc}."
    )
else:
    enviar_email(
        usuario['email'], 
        'EMC Ruim', 
        f"Seu IMC está ruim. Valor: {imc}."
    )

