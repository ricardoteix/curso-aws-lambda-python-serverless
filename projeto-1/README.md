# Curso AWS Lambda com Python e Serverless Framework
# Projeto 1

Neste projeto nós automatizamos um ambiente com instâncias EC2 e RDS para ligar e desligar estas instâncias para uso no horário comercial.

## Considerações para uso deste projeto

- Baixe este repositório.
- Acesse a pasta do **projeto-1**.
- No arquivo **lambda_function.py** você precisa especificar corretamente o ID da instância EC2 e RDS.
```python
def lambda_handler(event, context):
    
    print(event)
    
    # Trocar IDs para sua instância
    instance_id = 'i-04899716f68a927b3'
    rds_id = 'projeto1'
    
  ...
```
- No arquivo [policy.json](./policy.json) substitua as informações para refletir a sua conta da AWS:
    - ID_DA_CONTA_AWS: substitua pelo ID da sua conta AWS.
    - ID_DA_EC2: substitua pelo ID da instância EC2.
    - NOME_INSTANCIA_RDS: substitua pelo nome da instância RDS.
- Configure a CRON do seu EventBridge de acordo com o horário que deseja ligar ou desligar as instâncias. Conseidere este exemplo:
```
# LIGAR (GMT)
0    10    ?              *       2-6             *
Min  Hour  Day of month   Month   Day of week   Year

# DESLIGAR (GMT)
0    22     ?              *       2-6             *
Min  Hour  Day of month   Month   Day of week   Year
```
- Lembre-se de excluir todos os recursos quando finalizar este laboratório para evitar cobranças indesejadas.
- ATENÇÃO: instâncias RDS se ligam automaticamente 7 dias após desligadas.
