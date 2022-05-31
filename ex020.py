'''
O mesmo professor do desafio 019 quer
 sortear a ordem de apresentação de trabalhos dos alunos.
  Faça um programa que leia o nome dos quatro
   alunos e mostre a ordem sorteada.
'''
'''
from random import shuffle **SEM IMPORTAR TODA A BIBLIOTECA(tirar as referencias a random)**
'''
import random
a1=str(input('Digite o nome do 1° aluno: '))
a2=str(input('Digite o nome do 2° aluno: '))
a3=str(input('Digite o nome do 3° aluno: '))
a4=str(input('Digite o nome do 4° aluno: '))
lis= [a1, a2, a3, a4]
random.shuffle(lis)
print('A ordem será {}' .format(lis))

