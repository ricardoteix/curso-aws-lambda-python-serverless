import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_ec2 = sessao.client('ec2')

id_instancia = 'i-0297131342a087164'

cliente_ec2.terminate_instances(
    InstanceIds=[id_instancia]
)
