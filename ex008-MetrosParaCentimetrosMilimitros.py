'''
Escreva um programa que leia um valor em metros
 e o exiba convertido em centímetros e milímetros.
'''
n1=float(input('Digite a quantidade em metros: '))
n2=n1*100
n3=n1*1000
print('O valor em metros é {}, \n isto equivale a {:.0f} centimetros e \n'
      '{:.0f} milimetros' .format(n1, n2, n3))

