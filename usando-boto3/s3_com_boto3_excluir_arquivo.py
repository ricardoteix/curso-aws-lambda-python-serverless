import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_s3 = sessao.client('s3')

nome_bucket = 'curso-python-aws'

resource_s3 = sessao.resource('s3')
bucket = resource_s3.Bucket(nome_bucket)

objetos = bucket.objects.all()
# for obj in objetos:
#     print(obj)

resultado = objetos.delete()
print(resultado)

# resposta_delete = bucket.delete_objects(
#     Delete={
#         'Objects': [
#             {
#                 'Key': 'planilha.xls'
#             },
#             {
#                 'Key': 'demo.txt'
#             }
#         ]
#     }
# )
# print(resposta_delete)

# resposta = cliente_s3.delete_object(
#     Bucket=nome_bucket,
#     Key='imagens/img.jpg'
# )
# print(resposta)

