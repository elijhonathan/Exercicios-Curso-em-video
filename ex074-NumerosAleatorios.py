'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre
a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

n = (randint(1, 50), randint(1, 50), randint(1, 50),
     randint(1, 50), randint(1, 50))
for nu in n:
    print(f'{nu} ', end='')
print(f'\nO maior número foi {max(n)}')
print(f'O menor número foi {min(n)}')
