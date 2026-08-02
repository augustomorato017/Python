import time
def menu(msg):
    while True:
                #Título
        time.sleep(1)
        print('-'*30)
        print('Menu Principal'.center(30))
        print('-'*30)
        print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2 -\033[m \033[34mCadastrar uma nova pessoa\033[m')
        print('\033[33m3 -\033[m \033[34mEncerrar sessão\033[m')
        print('-'*30)
        opc = str(input(msg))
        print('-'*30)

                #Ver pessoas cadastradas
        if opc == '1':
            with open('lista.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                time.sleep(1)
                print(f'Pessoas Cadastradas'.center(30))
                print('-'*30)
                print(conteudo)
                print('-'*30)

                #Cadastrar uma nova pessoa
        elif opc == '2':
            nome = input('Nome: ')
            idade = input('Idade: ')
            with open('lista.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{nome:<15}')
                arquivo.write(f'{"{} anos".format(idade):>15}\n')

                #Encerrar o programa
        elif opc == '3':
            time.sleep(1)
            print('\033[31mEncerrando sessão...\033[m')
            break

                #Opção inválida
        else:
            print('\033[31mDigite uma opção válida!\033[m')

menu('\033[32mSua Opção: \033[m')