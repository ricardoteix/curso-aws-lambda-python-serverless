def calcular_idade():
    ano_nascimento = 1985
    ano_atual = 2023
    idade = ano_atual - ano_nascimento
    print(idade)

def informar_idade():
    print("Você fez:")
    calcular_idade()
    print('Parabéns!')

def enviar_email_erro():
    email = {
        'rementente': 'naoresponda@gmail.com',
        'destinatario': os.getenv('USER_EMAIL'),
        'assunto': 'Erro ao processar requisição',
        'mensagem': 'A requisição não pode ser realizada.'
    }
    send_email(email)

# print(informar_idade())
informar_idade()

