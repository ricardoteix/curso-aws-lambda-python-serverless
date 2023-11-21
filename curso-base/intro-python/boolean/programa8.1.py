# True : verdadeiro
# False: falso

ec2_ligado = True
rds_ligado = False

print(f'A instância ec2 está ligada? {ec2_ligado}')
print(f'O banco de dados está ligado? {rds_ligado}')

print(not True)
print(not False)

# x y AND
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

print(ec2_ligado and rds_ligado)

# x y OR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

print(ec2_ligado or rds_ligado)
