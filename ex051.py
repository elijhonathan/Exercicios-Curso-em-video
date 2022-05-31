'''
 Desenvolva um programa que leia o primeiro termo
  e a razão de uma PA. No final,
  mostre os 10 primeiros termos dessa progressão.
'''
prim=int(input('Digite o primeiro termo: '))
raz=int(input('Digite a razão: '))
dec= prim + (10 - 1) * raz
for c in range(prim, dec + raz, raz):
    print('{}' .format(c), end=' ->')
print('ACABOU')
