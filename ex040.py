'''
Crie um programa que leia duas notas de um aluno e calcule
 sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
if n1 > 10:
    print('Você digitou uma nota inválida, tente novamente.')
elif n2 > 10:
    print('Você digitou uma nota inválida, tente novamente.')
else:
    med= (n1 + n2) / 2
if med < 5:
    print('Sua média foi {}\n'
          'Você foi REPROVADO' .format(med))
elif med >= 5 and med <= 6.9:
    print('Sua média foi {}\n'
          'Você está de RECUPERAÇÃO' .format(med))
elif med >= 7:
    print('Sua média foi {}\n'
          'Você foi APROVADO \n PARABÉNS!' .format(med))
