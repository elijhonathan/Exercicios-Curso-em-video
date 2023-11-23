'''
 Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''
nome=str(input('Digite seu nome completo: ')) .strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas ficará {}' .format(nome.upper()))
print('Seu nome em letras minusculas ficará {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
corta=nome.split()
print(corta)
print('Seu primeiro nome é {} e ele tem  letras {}' .format(corta[0], len(corta[0])))

