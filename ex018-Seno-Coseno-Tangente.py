'''
 Faça um programa que leia um ângulo qualquer
  e mostre na tela o valor do
  seno, cosseno e tangente desse ângulo.
'''
'''
from math import sin, cos, tan, radians **SEM IMPORTAR TODA A BIBLIOTECA(TIRAR A REFERENCIA A MATH)**
'''
import math
ang=float(input('Digite o valor do ângulo: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('O ângulo {} tem como seno {:.2f}' .format(ang, sen))
print('O ângulo {} tem como cosseno {:.2f}' .format(ang, cos))
print('O ângulo {} tem como tangente {:.2f}' .format(ang, tan))


