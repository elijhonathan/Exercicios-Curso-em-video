'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
joken= ('Pedra', 'Papel', 'Tesoura')
comp= randint(0, 2)
print('{:=^25}' .format(' Vamos Jogar JOKENPÔ? '))
print('''
[0] Pedra
[1] Papel
[2] Tesoura
''')
esc=int(input('Boa sorte \nDigite sua escolha: '))
print('-=' * 10)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('O JOGADOR escolheu {}' .format(joken[esc]))
sleep(1)
print('O COMPUTADOR escolheu {}' .format(joken[comp]))
sleep(1)
print('-=' * 10)
if comp==0:#computador escolheu Pedra
    if esc ==0:
        print('EMPATE')
    elif esc==1:
        print('JOGADOR GANHOU')
    elif esc==2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida, Tente novamente!')
elif comp==1:#computador escolheu Papel
    if esc==0:
        print('COMPUTADOR GANHOU')
    elif esc==1:
        print('EMPATE')
    elif esc==2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada inválida, Tente novamente!')
elif comp==2:#computador escolheu Tesoura
    if esc==0:
        print('JOGADOR GANHOU')
    elif esc==1:
        print('COMPUTADOR GANHOU')
    elif esc==2:
        print('EMPATE')
    else:
        print('Jogada inválida, Tente nvoamente!')
