'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
vc=float(input('Qual o valor da casa?: R$  '))
sc=float(input('Qual o seu salário?: R$ '))
qa=int(input('Em quantos anos pretende pagar?: '))
ps= sc * 0.30
na= qa * 12
me= vc / na

if me > ps:
    print('Seu emprestimo foi negado')
elif me == ps:
    print('Seu emprestimo foi aceito')
else:
    print('Seu emprestimo foi aceito')
print('O valor da parcela é R$ {:.2f} ' .format(me))
