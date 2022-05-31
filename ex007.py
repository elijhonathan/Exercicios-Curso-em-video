'''
Desenvolva um programa que leia as duas notas
 de um aluno, calcule e mostre a sua média.
'''
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=n1+n2
n4=n3/2
print('A primeira nota foi {}, a segunda nota foi {} \n a sua média é {:.1f}'
      .format(n1, n2, n4))
