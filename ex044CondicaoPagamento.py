'''
Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^50}' .format(' Lojas Python '))
produto=float(input('Qual o valor total das compras?: R$ '))
print(''' Informe a forma de pagamento:
[1] à vista no dinheiro/ cheque:
[2] à vista no cartão:
[3] em até 2x no cartão:
[4] 3x ou mais no cartão:
''')
esc=int(input('Escolha sua opção: '))
if esc ==1:
    print('No pagamento à vista no dinheiro/ cheque \n'
          'O valor de R$ {:.2f} sairá com desconto de 10%\n'
          'O valor a ser pago será R$ {:.2f}' .format(produto, produto - (produto * 0.10 )))
elif esc ==2:
    print('No pagamento à vista no cartão\n'
          'O valor de R$ {:.2f} sairá com desconto de 5%\n'
          'O valor a ser pago será R$ {:.2f}' .format(produto, produto -(produto *0.05)))
elif esc ==3:
    print(' No pagamento em até 2x no cartão\n'
          'O Valor de R$ {:.2f} sairá SEM JUROS!\n'
          'Em duas parcelas de R$ {:.2f}'.format(produto, produto / 2))
elif esc ==4:
    print('No pagamento 3x ou mais no cartão\n'
          'O valor de R$ {:.2f} terá um acrésimo de 20% de juros mais 1% por parcela' .format(produto))
    nparc=int(input('informe o número de parcelas(3x ou mais): ' .format(produto)))
    print('Com {} parcelas o valor a ser pago será R$ {}\n'
          'Em {} de R$ {:.2f}'
          .format(nparc, produto + (produto * 0.20) +(produto * (nparc /100 )), nparc,
                  (produto + (produto * 0.20) +(produto * (nparc /100 ))) / nparc))
else:
    print('Você digitou uma opção inválida\n'
          'Tente novamente!')
