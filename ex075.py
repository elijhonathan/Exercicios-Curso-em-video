'''
Desenvolva um programa que leia quatro
valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
nu = (int(input('Digite o primeiro valor: ')),
int(input('Digite o segundo valor: ')),
int(input('Digite o terceiro valor: ')),
int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {nu}')
print(f'O número 9 apareceu {nu.count(9)} vezes')
if 3 in nu:
    print(f'O número 3 foi digitado na {nu.index(3) +1}° posição')
else:
    print('O número 3 não foi digitado!')
print('Os valores pares digitados foram ', end='')
for n in nu:
    if n % 2 == 0:
        print(n, end=', ')


