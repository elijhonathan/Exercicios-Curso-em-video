'''
Melhore o jogo do DESAFIO 028 onde o computador
 vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar
 até acertar, mostrando no
 final quantos palpites foram necessários para vencer.
'''
from random import randint
cont=0
sort= randint(1,10)
acertou= False
while not acertou:
    num = int(input('Digite um número de 0 a 10 para tentar adivinhar: '))
    cont += 1
    if num == sort:
        acertou = True
    elif num != sort and num > sort:
        print('Você errou tente novamente, o número é menor:')
    elif num != sort and num < sort:
        print('Você errou tente novamente, o número é maior:')
print('O número sorteado foi {} e você acertou na tentativa {}' .format(sort, cont))
