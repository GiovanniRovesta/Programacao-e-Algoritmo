senhac = 6777
tentativas = 1
limitet = 5

senha = int(input('Descubra a senha de 4 números: '))

while senha != senhac and tentativas < limitet:
    print('Senha incorreta, tente novamente. \n')
    senha = int(input('Descubra a senha de 4 números: '))
    tentativas += 1
if senha == senhac:
    print('Acesso liberado')
else:
    print('Acesso negado')
