'''
Faça um algoritmo que leia o preço de um produto
 e mostre seu novo preço, com 5% de desconto.
'''
val=int(input('Digite o valor do produto: R$ '))
des1=0.05
des2=val*des1
des3=val-des2
print('O valor do produto com desconto será R$ {:.2f} \n'
      'Você ganhou um desconto de R$ {:.2f}' .format(des3, des2))
