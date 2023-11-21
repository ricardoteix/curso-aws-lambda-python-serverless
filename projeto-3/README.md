# Curso AWS Lambda com Python e Serverless Framework
# Projeto 3

Neste projeto nós automatizamos o envio uma mensagem para um grupo no Telegram. 
Esta mensagem vai conter o custo da conta AWS em questão.

## Considerações para execução deste projeto

- Baixe este repositório.
- Acesse a pasta do **projeto-3**.
- Certifique de realizar as configurações necessárias no Telegram e atualize o arquivo **app.py** com o **bot_token** e **id_canal** obtidos por você.
- Atualize arquivo serverless.yml com suas credentiais e região da AWS que quer usar, como no código abaixo.

```yaml
provider:
  name: aws
  runtime: python3.9
  profile: automacao-curso
  region: us-east-1
  ...
```
- Se for executar localmente o código Python não esqueça de criar, ativar e instalar os requisitos do ambiente
```bash
~/projeto-3/> python -m venv env
~/projeto-3/> .\env\Scripts\activate
~/projeto-3/> pip install -r requirements.txt
```
- Execute o comando **deploy** para criar a infra na AWS.
```bash
~/projeto-3/> serverless deploy
```
- Para remover toda a infra criada, execute o comando **remove**.
```bash
~/projeto-3/> serverless remove
```
- Se preciso exclua o bot e o canal do Telegram.

## Diagrama
![Diagrama](./docs/projeto-3.drawio.png)
