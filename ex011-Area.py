'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária para
 pintá-la, sabendo que cada litro de tinta pinta
 uma área de 2 metros quadrados.
'''
lar=float(input('Quantos metros de largura?: '))
alt=float(input('Quantos metros de altura?: '))
mq=lar*alt
lt=mq/2
print('Com a largura de {} metros e a altura de {} metros \n'
      'você precisará de {:.2f} litros de tinta para cobrir {:.2f} m² de area. ' .format(lar, alt, lt, mq))
