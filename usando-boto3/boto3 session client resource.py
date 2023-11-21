import boto3

sessao = boto3.Session(profile_name="automacao-curso")

cliente_s3 = sessao.client('s3')
client_ec2 = sessao.client('ec2')

lista = cliente_s3.list_buckets()
# print(lista)

recurso_s3 = sessao.resource('s3')
bucket = recurso_s3.Bucket('saudacoes')
print(bucket)


