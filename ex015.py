'''
 Escreva um programa que pergunte a
 quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar,
 sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
qkm=float(input('Digite o número de Km rodados: '))
qdi=float(input('Digite a quantidade de dias que o carro foi alugado: '))
qdi2=qdi * 60
qkm2=qkm * 0.15
tot=qdi2 + qkm2
print('O carro alugado por {} dias e rodado {} km \n'
      'Terá o valor total de R$ {:.2f} a ser pago' .format(qdi, qkm, tot))
