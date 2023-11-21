import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_ec2 = sessao.client('ec2')

resposta_instancias = cliente_ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
                'stopped'
            ]
        },
    ],
)
# print(resposta_instancias)
id_instancias = resposta_instancias['Reservations'][0]['Instances'][0]['InstanceId']

print(id_instancias)

# Para / desliga a instância
# cliente_ec2.stop_instances(InstanceIds=[id_instancias])

# Inicializa / liga a instância
cliente_ec2.start_instances(InstanceIds=[id_instancias])
