nome = str(input('Digite seu nome:'))
if nome == 'José':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Pedro' or nome == 'joaquim':
    print('Seu nome é bem popular no Brasil.')
else: 
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))