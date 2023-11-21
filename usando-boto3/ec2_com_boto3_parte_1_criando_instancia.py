import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_ec2 = sessao.client('ec2')

nome_chave = 'automacao.pem'
vpc_id = 'vpc-05024256a59257492'
subnet_id = 'subnet-0c3eb6c12df88ee73'
ami_id = 'ami-053b0d53c279acc90'

try:
    resposta_sg = cliente_ec2.create_security_group(
        Description='Novo sg',
        GroupName='sg_web',
        VpcId=vpc_id
    )
    sg_id = resposta_sg['GroupId']
    
    resposta_ingress = cliente_ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'ToPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso SSH'
                    }
                ]
            },
            {
                'FromPort': 80,
                'ToPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso HTTP'
                    }
                ]
            }
        ]
    )

except Exception as erro:
    print('sg_web já existe!')
    resposta_grupos = cliente_ec2.describe_security_groups(
        GroupNames=['sg_web']
    )
    sg_id = resposta_grupos['SecurityGroups'][0]['GroupId']
