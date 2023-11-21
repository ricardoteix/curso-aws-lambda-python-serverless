import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_s3 = sessao.client('s3')

nome_bucket = 'curso-python-aws'

resource_s3 = sessao.resource('s3')
bucket = resource_s3.Bucket(nome_bucket)

# cliente_s3.delete_bucket(Bucket=nome_bucket)
bucket.delete()
