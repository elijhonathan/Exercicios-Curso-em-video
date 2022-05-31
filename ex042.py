'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
 de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
s1=float(input('Digite o primeiro segmento: '))
s2=float(input('Digite o segundo segmento: '))
s3=float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos digitados PODEM formar um TRIANGULO ' , end='')
    if s1==s2==s3:
        print('Equilátero')
    elif s1!= s2 != s3 != s1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos digitados NÃO podem formar um TRIANGULO')
