ano = int(input('Digite um ano: '))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} é \033[34mbissexto\033[m.'.format(ano))
else:
    print('O ano {} \033[36mnão é bissexto\033[m.'.format(ano))