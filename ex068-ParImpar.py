'''
Faça um programa que jogue par ou ímpar com
o computador. O jogo só será interrompido quando o
 jogador perder, mostrando o total de
 vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v=0
while True:
    jogador= int(input('Digite um valor: '))
    computador= randint(1, 10)
    total= computador + jogador
    tipo= ' '
    while tipo not in 'PI':
        tipo=str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} o computador {computador} total {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo =='P':
        if total % 2 ==0:
            print('Você venceu')
            v += 1
        else:
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('Você venceu')
            v += 1
        else:
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! \nVocê venceu {v} vezes')
