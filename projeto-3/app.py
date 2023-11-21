import requests

# https://api.telegram.org/bot{{TOKEN}}/getUpdates

bot_token = 'MEU_TOKEN_TELEGRAM'
id_canal = 'ID_DO_MEU_CANAL'

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

def enviar_mensagem_telegram(mensagem):
    resposta = requests.post(
        api_url,
        json={
            "chat_id": id_canal,
            "text": mensagem
        }
    )