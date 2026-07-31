import random
n = [random.randint(1, 100) for c in range(5)]
print(f'Os números escolhidos foram: {n}')
print(f'O maior número é {max(n)}')
print(f'O menor número é {min(n)}')