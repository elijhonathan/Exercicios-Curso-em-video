'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp=str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
#print(f'Você digitou os valores {num}')
print(f'Você digitou {len(num)} valores.')
num.sort(reverse=True)
print(f'Os valores de forma decrescente fica {num}')
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
