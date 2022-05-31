'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC)
 e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
peso=float(input('Digite o seu peso em kg: '))
altura=float(input('Digite sua altura em metros: '))
imc= peso / (altura ** 2)
print('Seu IMC é {:.1f}' .format(imc))
if imc > 40:
    print('Você está na categoria: Obesidade Mórbida!')
elif imc > 30 and imc <= 40:
    print('Você está na categoria: Obesidade')
elif imc > 25 and imc <=30:
    print('Você está na categoria: Sobrepeso')
elif imc > 18.5 and imc <= 25:
    print('Você está na categoria: Peso Ideal')
elif imc > 1 and imc <= 18.5:
    print('Você está na categoria: Abaixo do Peso')
else:
    print('Você informou algum valor incorreto. \n Tente novamente!')

