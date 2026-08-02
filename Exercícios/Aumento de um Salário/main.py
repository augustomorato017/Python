sal = float(input('Digite o valor do seu salário atual:'))
if sal > 1250:
    aumento = sal * 0.10
else:
    aumento = sal * 0.15
nsal = sal + aumento
print('O novo salário é R${:.2f}, e o aumento foi de R${:.2f}'.format(nsal, aumento))