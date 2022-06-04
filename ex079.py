'''
Crie um programa onde o usuário possa digitar vários valores numéricos
 e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
num = list()
while True:
    n=int(input('Digite um valor : '))
    if n not in num:
        num.append(n)
        print('Valor adicionado...')
    else:
        print('Valor duplicado, Não vou adicionar...')
    r=str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Você digitou os valores {sorted(num)}')
