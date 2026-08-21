soma = 0
contador = 0

while True:
    nota = float(input('Digite uma nota de 1 a 10, para continuar, digite um número fora da área: '))
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    else:
        break
if contador > 0:
    media = soma / contador
    print(f'A média das {contador} notas válidas é: {media:.2f}')
else:
    print('Nenhuma nota válida foi digitada.')
