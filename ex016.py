'''
Crie um programa que leia um número Real qualquer
 pelo teclado e mostre na tela a sua porção Inteira.
'''
'''
import math **IMPORTANDO TODA A BIBLIOTECA**
'''
from math import trunc
int=float(input('Digite um valor: '))
'''
print('O valor digitado foi {} e a sua porção inteira é {}' .format(int, math.trunc(int))) 
**IMPORTANDO TODA A BIBLIOTECA**
'''
print('O valor digitado foi {} e a sua porção inteira é {}' .format(int, trunc(int)))
