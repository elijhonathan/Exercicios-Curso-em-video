'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se
  alistar ao serviço militar, se é a hora exata de se alistar
   ou se já passou do tempo do alistamento.
   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
an=int(input('Digite o seu ano de nascimento: '))
ano= date.today().year
idade= int( ano - an)
if an > ano:
    print('Você colocou um ano de nascimento não válido, tente novamente')
elif idade > 21 :
    print('Você já passou {} anos da idade máxima para se alistar \n'
          'Você deveria ter se alistado nos anos de {} a {}'
          .format(idade - 21, ano - (idade -21) - 3, ano - (idade - 21) ))
elif idade < 18  :
    print('Falta {} anos para idade minima para se alistar \n'
          'Os anos que você deverá se alistar é de {} a {}'
          .format(18 - idade, ano + (18 - idade),  (18 -idade) + ano + 3  ))
elif idade <= 21 and idade >= 18 :
    print('Você está na idade de alistamento \n'
          'Você tem até {} para se alistar' .format(ano + ( 21 - idade)  ))
