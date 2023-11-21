import boto3

# print(boto3)

sessao = boto3.Session(profile_name="automacao-curso")
cliente_s3 = sessao.client('s3')
lista = cliente_s3.list_buckets()
print(lista)