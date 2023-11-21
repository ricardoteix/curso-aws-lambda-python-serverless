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


arquivo_user_data = open('ec2/wp_user_data.sh', 'r')
user_data = arquivo_user_data.read()

resposta_ec2 = cliente_ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 8,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2',
                'Encrypted': False
            }
        }
    ],
    UserData=user_data,
    ImageId=ami_id,
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro',
    KeyName=nome_chave,
    Monitoring={
        'Enabled': False
    },
    SecurityGroupIds=[sg_id],
    SubnetId=subnet_id,
    InstanceInitiatedShutdownBehavior='terminate',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'wp-curso-python'
                },
                {
                    'Key': 'Ambiente',
                    'Value': 'desenvolvimento'
                }
            ]
        }
    ]
)
print(resposta_ec2)