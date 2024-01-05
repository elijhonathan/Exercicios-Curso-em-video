'''
Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores
  pares e os valores ímpares digitados, respectivamente.
  Ao final, mostre o conteúdo das três listas geradas.
'''

lista = list()
pares = list()
impares= list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp=str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados foram {lista}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')




