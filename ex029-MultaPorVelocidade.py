'''
Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
  multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel=int(input('Digite a velocidade do carro: '))
mult= vel - 80
valor= mult * 7
if vel > 80:
    print('Sua velocidade utrapassou o limite permitido \n Você foi multado em R$ {:.2f}' .format(valor))
if vel <  80:
    print('Sua velocidade está dentro do permitido \n Você não foi multado')
if vel == 80:
    print('Sua velocidade está dentro do permitido \n Você não foi multado')
