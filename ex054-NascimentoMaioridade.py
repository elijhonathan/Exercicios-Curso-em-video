'''
Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import date
atual= date.today().year
totmaior=0
totmenor=0
for pes in range(1,8):
    nas=int(input('Digite o {}° ano de nascimento: '.format(pes)))
    idade = atual - nas
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade' .format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade' .format(totmenor))
