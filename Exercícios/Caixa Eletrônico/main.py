resp = 'S'
n50 = n20 = n10 = n1 = 0
#50 20 10 1
while resp == 'S':
    valor = n50 = n20 = n10 = n1 = 0
    valor = int(input('Digite o valor a ser sacado: R$ '))
    while valor >= 50:
        n50 += 1
        valor -= 50
    while valor >= 20:
        n20 += 1
        valor -= 20
    while valor >= 10:
        n10 += 1
        valor -= 10
    while valor >= 1:
        n1 += 1
        valor -= 1
    print(f'Notas de R$50: {n50}')
    print(f'Notas de R$20: {n20}')
    print(f'Notas de R$10: {n10}')
    print(f'Notas de R$1: {n1}')
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
