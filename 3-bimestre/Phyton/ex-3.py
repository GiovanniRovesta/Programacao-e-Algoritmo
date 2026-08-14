n = int(input('Escolha um número inteiro: '))
contador = 1

if n > 0:
    while contador <= n:
        print(f'{contador}')
        contador += 1
else:
    print('Seu número é invalido')
