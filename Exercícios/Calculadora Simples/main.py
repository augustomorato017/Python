n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
c = 0
while c != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    c = int(input('Digite a opção desejada: '))
    if c == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    if c == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    if c == 3:
        print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    if c == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('Fim do Programa!')