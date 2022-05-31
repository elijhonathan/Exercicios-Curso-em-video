'''
Escreva um programa que converta uma
temperatura digitando em graus Celsius
 e converta para graus Fahrenheit.
'''
c= float(input('Digite a temperatura em C°: '))
f= ( (9 * c) / 5) + 32
print(' {:.0f} C° equivale a {:.0f} F°' .format(c, f))
f2= float(input('Digite a temperatura em F°: '))
c2= ((f2 - 32) / 9) * 5
print(' {:.0f} F° equivale a {:.0f} C°' .format(f2, c2))

