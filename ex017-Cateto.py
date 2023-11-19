'''
Faça um programa que leia o comprimento do cateto oposto
 e do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa.
'''

'''import math **IMPORTANDO TODA A BIBLIOTECA**
'''
from math import hypot
caop=float(input('Qual o comprimento do cateto oposto: '))
caad=float(input('Qual o comprimento do cateto adjacente: '))
'''
hi= (caop ** 2 + caad ** 2 ) ** (1/2) *FORMULA MATEMATICA*
'''
'''
hi= math.hypot(caop, caad) **IMPORTANDO TODA A BIBLIOTECA**
'''
hi=hypot(caop, caad)
print('A hipotenusa será {:.2f}' .format(hi))
