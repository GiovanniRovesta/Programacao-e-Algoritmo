div = 1
qdiv = 0

n = int(input('Digite um número inteiro positivo: '))

if n > 0:
    while div <= n:
        if n % div == 0:
            qdiv += 1
        div += 1
    if qdiv == 2:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
else:
    print('O número é inválido')
