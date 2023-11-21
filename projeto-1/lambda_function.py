import json
import boto3

cliente_ec2 = boto3.client('ec2')
cliente_rds = boto3.client('rds')

def lambda_handler(event, context):
    
    print(event)
    
    # Trocar IDs para sua instância
    instance_id = 'i-04899716f68a927b3'
    rds_id = 'projeto1'
    
    ligar = 'projeto1-start' in event['resources'][0]
    desligar = 'projeto1-stop' in event['resources'][0]
    
    if ligar:
        cliente_ec2.start_instances( InstanceIds=[instance_id] )
        cliente_rds.start_db_instance ( DBInstanceIdentifier=rds_id )
        mensagem = "Instâncias inicializadas."
    elif desligar:
        cliente_ec2.stop_instances( InstanceIds=[instance_id] )
        cliente_rds.stop_db_instance ( DBInstanceIdentifier=rds_id )
        mensagem = "Instâncias paradas."
    else:
        mensagem = "Nunhuma instância mudou de estado."
        
    print('Mensagem: ' , mensagem)
    
    return {
        'statusCode': 200,
        'body': mensagem
    }
