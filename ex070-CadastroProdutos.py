'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
togaco= quprcu1000 = cont = 0
prmaba=' '
while True:
    nomepro=str(input('Digite o nome do produto: '))
    valorpro=float(input('Digite o valor do produto: R$ '))
    cont += 1
    togaco += valorpro
    if valorpro > 1000:
        quprcu1000 = + 1
    if cont ==1 or valorpro < menor:
        menor=valorpro
        prmaba=nomepro

    resp=' '
    while resp not in 'SN':
         resp=str(input('Gostaria de cadastrar mais produtos?: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'O valor total gasto na compra foi R$ {togaco}0')
print(f'{quprcu1000} produtos custam mais de R$ 1000.00')
print(f'{prmaba} é o produto mais barato e custa {menor:.2f}.')
