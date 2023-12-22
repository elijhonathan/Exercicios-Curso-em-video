'''
Melhore o DESAFIO 061, perguntando para o usuário s
e ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão PA: '))
termo= primeiro
cont= 1
total= 0
mais= 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais?: '))
print('Programação finalizada com total {} de vezes executada'.format(total))
