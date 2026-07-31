idade = int(input('Digite a sua idade: '))
if idade == 18:
    print('\033[33mVocê deve se alistar imediatamente!\033[m')
elif idade < 18:
    print('\033[32mAinda faltam {} anos para o seu alistamento.\033[m'.format(18 - idade))
else:
    print('\033[31mVocê já deveria ter se alistado há {} anos!\033[m'.format(idade - 18))