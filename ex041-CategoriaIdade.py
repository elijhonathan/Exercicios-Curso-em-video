'''
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date
ano=int(input('Digite o ano do seu nascimento: '))
anoatual=date.today().year
idade = anoatual - ano
if idade >= 120:
    print('Você tem {} anos \n'
          'Você é a pessoa mais velha do mundo \n'
          'PARABÉNS!' .format(idade))
elif idade > 25:
    print('Você tem ou fará {} anos \n'
          'Sua categoria será a MASTER' .format(idade))
elif idade <= 25 and idade >= 20:
    print('Você tem ou fará {} anos \n'
          'Sua categoria será a SÊNIOR' .format(idade))
elif idade <= 19 and idade >= 15:
    print('Você tem ou fará {} anos \n'
        'Sua categoria será a JÚNIOR' .format(idade))
elif idade <= 14 and idade >= 10:
    print('Você tem ou fará {} anos \n'
        'Sua categoria será a INFANTIL' .format(idade))
elif idade <=9 and idade > 1:
    print('Você tem ou fará {} anos \n'
        'Sua caregoria será a MIRIM' .format(idade))
elif idade == 1:
    print('Você tem ou fará {} ano \n'
        'Sua caregoria será a MIRIM' .format(idade))
else:
    print('Você digitou um ano inválido \n Tente novamente!')
