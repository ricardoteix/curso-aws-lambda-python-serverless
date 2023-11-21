import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_s3 = sessao.client('s3')

nome_bucket = 'curso-python-aws'

cliente_s3.download_file(
    nome_bucket,
    'imagens/img.jpg',
    'arquivos/foto.jpg'
)

arquivo = open('arquivos/foto2.jpg', 'wb') # wb -> Write Binary
cliente_s3.download_fileobj(
    nome_bucket,
    'imagens/img.jpg',
    arquivo
)
arquivo.close()

planilha_s3 = cliente_s3.get_object(
    Bucket=nome_bucket,
    Key='planilha.xls'
)
planilha_body = planilha_s3['Body']
planilha = planilha_body.read()
print(type(planilha))
print(planilha)
print(planilha.decode('utf8'))
