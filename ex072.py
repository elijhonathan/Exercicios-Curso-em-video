'''
Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
e após mostrar a resposta perguntar se deseja continuar ou sair do programa.
'''
nupoex=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
        'Dezoito', 'Dezenove', 'Vinte')

while True:
        num=int(input('Digite um número de 0 á 20 para ver sua escrita por extenso: '))
        if num > 20 or num < 0:
                print('Numero inválido, Tente novamente!')
        elif num <= 20 and num >=0:
                print(f'Você digitou {num} e a sua escrita por extenso é {nupoex[num]}')
                while True:
                        continuar=str(input('Gostaria de Continuar? [S/N]: ')).strip().upper()
                        if continuar == 'N':
                                break
                        if continuar == 'S' or continuar == 'N':
                                break
                if continuar == 'N':
                        break
print('Obrigado por usar nosso programa.')


