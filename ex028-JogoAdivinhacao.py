'''
Escreva um programa que faça o computador "pensar"
 em um número inteiro entre 0 e 5 e peça para o usuário tentar
  descobrir qual foi o número escolhido pelo computador.
  O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
computador= randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número de 0 a 5 tente adivinhar')
print('-=-' * 10)
num=int(input('Digite um número: '))
print('Processando...')
sleep(1)
if num == computador:
    print('Parabuens! Você acertou o número que pensei.')
else:
    print('Você errou, eu pensei no número {} e não no {}' .format(computador, num))
