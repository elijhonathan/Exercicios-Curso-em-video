'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a
R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
sal=float(input('Digite o valor do seu sálario: R$ '))
n1=0.10
n2= 0.15
if sal == 1250:
    print('O seu novo salário é R$ {:.2f}' .format((sal * n1) + sal))
if sal > 1250:
    print('O seu novo salário é R$ {}' .format((sal * n1) + sal))
if sal < 1250:
    print('O seu novo salário é R$ {}' .format((sal * n2) + sal))


