'''
Faça um programa que leia
algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
'''

n1= input('Digite algo: ')
print ('O tipo primitivo desse valor é', type(n1))
print ('Só tem espaços? ', n1.isspace())
print ('É só números? ', n1.isnumeric())
print('É alfanumérico? ', n1.isalpha())
print('É só letras maiusculas?', n1.isupper())
print('É só letras minusculas', n1.islower())
print('Está capitalizada?', n1.istitle())

