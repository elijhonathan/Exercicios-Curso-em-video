'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
#from math import factorial
n1=int(input('Digite um número inteiro para ver seu fatorial: '))
c= n1
f= 1
print('Calculando {}! ='.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(' {}'.format(f))

