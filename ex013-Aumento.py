'''
Faça um algoritmo que leia o salário de um funcionário
 e mostre seu novo salário, com 15% de aumento.
'''
sal=float(input('Digite seu salário atual: R$ '))
nov= sal + (sal * 15 / 100)
aum= sal * 15 / 100
print('O seu novo salário será R$ {:.2f} \n'
      'Você ganhou um aumento de R$ {:.2f} ' .format(nov, aum))
