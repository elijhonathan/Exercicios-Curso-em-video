'''
Faça um programa que leia o nome completo
 de uma pessoa, mostrando em seguida o primeiro e o último nome
'''
nome=str(input('Digite o seu nome completo: ')) .strip()
n=nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu último nome é {}' .format(n[len(n) - 1 ]))
