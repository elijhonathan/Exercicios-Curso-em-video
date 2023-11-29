'''
Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para
viagens de até 200Km
 e R$0,45 parta viagens mais longas.
'''
km=float(input('Quantos km você percorreu?: '))
if km <= 200:
    print('Sua viagem deu RS {:.2f}' .format(km * 0.50))
else:
    print('Sua viagem deu R$ {:.2f}' .format(km * 0.45))
