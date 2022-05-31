'''
Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os
  valores e qual foi o maior e o menor valores lidos.
  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
soma= media = quant = maior = menor = 0
while resp in 'Ss':
    n1=int(input('Digite um número inteiro: '))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior= n1
        if n1 < menor:
            menor=n1
    resp=str(input('Gostaria de continuar? [S/N]: ')).upper().strip()[0]
media= soma / quant
print('Você digitou {} números e a média é {:.2f}'.format(quant, media))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))
