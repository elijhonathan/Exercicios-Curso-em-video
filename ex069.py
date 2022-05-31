'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
pema18 = quho = mume20 = 0
while True:
    idade=int(input('Digite a idade: '))
    sexo=' '
    while sexo not in'MF':
        sexo=str(input('Digite o sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        pema18 += 1
    if sexo == 'M':
        quho += 1
    if idade < 20 and sexo == 'F':
        mume20 += 1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Gostaria de continuar?:[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{pema18} pessoas tem mais de 18 anos')
print(f'{quho} homens foram cadastrados')
print(f'{mume20} mulheres tem menos de 20 anos')
