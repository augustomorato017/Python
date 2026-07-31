import random
n = int(0)
tentativas = 0
print('\033[31mBem-vindo ao jogo de adivinhação!\033[m')
ns = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
while n != ns:
    n = int(input('Digite um número entre 1 a 10: '))
    tentativas += 1
if n == ns:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou! O número era {}{}{}.'.format('\033[32m' , ns, '\033[m'))
print('Você tentou {} vezes.'.format(tentativas))