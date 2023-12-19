'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
import  math
from time import sleep
quatro= False
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
esc=0

while esc != 5:
    print('Você digitou {} e {}, o que deseja fazer a seguir: '.format(n1, n2))
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
    esc=int(input('Digite sua opção: '))
    if esc == 1:
            print('A soma de {} e {} será {}'.format(n1, n2, n1 + n2))
    elif esc == 2:
            print('A multiplicação de {} e {} será {}'.format(n1, n2, n1 * n2))
    elif esc == 3:
        if n1 > n2:
            n3=n1
        else:
            n3=n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, n3 ))
    elif esc==4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif esc==5:
            print('Obrigado por usar o nosso programa')
    else:
            print('Opção inválida, tente novamente')
    sleep(2)




