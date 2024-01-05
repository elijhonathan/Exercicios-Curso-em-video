'''
Crie um programa onde o usuário digite uma expressão qualquer
 que use parênteses. Seu aplicativo deverá analisar se a
 expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expr=str(input('Digite uma expressão: '))
pare = []
for simb in expr:
    if simb == '(':
        pare.append('(')
    elif simb == ')':
        if len(pare) > 0:
            pare.pop()
        else:
            pare.append(')')
            break
if len(pare) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
