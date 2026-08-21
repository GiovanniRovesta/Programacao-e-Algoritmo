contador = 1
soma = 0

n = int(input('Digite um número positivo: \n'))
if n > 0:
    while contador <= n:
        if contador % 2 == 0:
            soma = contador + soma
        contador += 1
    print(f'A soma dos pares é: {soma}')
else:
    print('Número inválido')
