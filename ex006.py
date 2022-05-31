'''
Crie um algoritmo que leia um número e mostre
 o seu dobro, triplo e raiz quadrada.
'''
n1=int(input('Digite um número: '))
n2=n1*2
n3=n1*3
n4=n1**(1/2)
print('O número escolhido foi {}, o dobro é {}, o triplo é {} e \n a raiz quadrada é {:.2f}'
      .format(n1, n2, n3, n4))


