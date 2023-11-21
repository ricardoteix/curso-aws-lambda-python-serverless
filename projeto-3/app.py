import requests

# https://api.telegram.org/bot{{TOKEN}}/getUpdates

bot_token = '6562601245:AAFjBAXU2Vv6TpljXgCAw0EVZXbUrbTZ68s'
id_canal = '-1002128690041'

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

def enviar_mensagem_telegram(mensagem):
    resposta = requests.post(
        api_url,
        json={
            "chat_id": id_canal,
            "text": mensagem
        }
    )