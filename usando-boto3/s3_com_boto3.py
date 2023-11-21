import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_s3 = sessao.client('s3')

nome_bucket = 'curso-python-aws'

try:

    resposta_bucket = cliente_s3.create_bucket(
        Bucket=nome_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )
    # print(resposta_bucket)

except Exception as err:
    print('Este bucket já existe')
    
cliente_s3.upload_file(
    'arquivos/aws_light_theme_logo.svg',
    nome_bucket,
    'imagens/aws_logo.svg'
)

planilha = """
    Nome\tNota
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\t10
"""

cliente_s3.put_object(
    Body=planilha,
    Bucket=nome_bucket,
    Key='planilha.xls'
)
