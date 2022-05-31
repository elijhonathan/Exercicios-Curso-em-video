'''
Um professor quer sortear um dos seus quatro alunos
 para apagar o quadro. Faça um programa que ajude ele,
  lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
'''
from random import choice **SEM IMPORTAR A BIBLIOTECA INTEIRA(TIRAR A REFERENCIA RANDOM)**
'''
import random
a1=str(input('Digite o nome do 1° aluno: '))
a2=str(input('Digite o nome do 2° aluno: '))
a3=str(input('Digite o nome do 3° aluno '))
a4=str(input('Digite o nome do 4° aluno: '))
lista= [a1, a2, a3, a4]
esc= random.choice(lista)
print('O escolhido foi {}' .format(esc))
