'''
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas
 podem ou não formar um triângulo.
'''
s1=float(input('Digite o primeiro segmento: '))
s2=float(input('Digite o segundo segmento: '))
s3=float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos digitados PODEM formar um TRIANGULO')
else:
    print('Os segmentos digitados NÃO podem formar um TRIANGULO')
