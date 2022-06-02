'''
Crie uma tupla preenchida com os 20 primeiros colocados da
 Tabela do Campeonato Brasileiro (SERIE B) de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
#CODIGO PEDIDO NA AULA ESTÁ ENTRE ''', ABAIXO MENU INTERATIVO QUE FIZ A PARTE!!!!!!!!!
'''print('--' * 80)
print(f'Lista de times do Brasileirão seríe B por colocação: {times}')
print('--' * 80)
print(f'Os cinco primeiros são : {times[0:5]}')
print('--' * 80)
print(f'Os 4 ultímos são: {times[-4:]}')
print('--' * 80)
print(f'A ordem alfabética é : {sorted(times)}')
print('--' * 80)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}° posição')
print('--' * 80)'''

times = ('Cruzeiro', 'Vasco da Gama', 'Bahia', 'Sport', 'Grêmio', 'Novorizontino',
       'Operário PR', 'Sampaio Corrêa', 'Londrina', 'Chapecoense', 'Csa',
       'Brusque', 'Crb', 'Ituano', 'Criciúma', 'Ponte Preta', 'Náutico',
       'Tombense', 'Vila Nova', 'Guarani')

while True:
       cont = 1
       detras = 20
       print('Bem vindo a Tabela do\nCampeonato Brasileiro seríe B')
       print('''[1] Ver a Atual Colocação:
[2] Ver os Primeiros:
[3] Ver os Ultímos:
[4] Ver os times em ordem alfabética:
[5] Ver a posição de algum time específico:
[6] Sair:''')
       opcao=int(input('Digite uma opção: '))
       if opcao > 6 or opcao < 1:
              print('Opção inválida, Tente novamente!')
       if opcao == 6:
              break
       if opcao == 1:
              for t in times:
                     print(f'{cont}° lugar {t}')
                     cont += 1

       if opcao == 2:
              n=int(input('Em ordem crescente quanto dos primeiros gostaria de ver: '))
              for t in times[:n]:
                     print(f'{cont}° lugar {t}')
                     cont += 1
       if opcao == 3:
              n=int(input('Em ordem descrecente quanto dos ultimos gostaria de ver: '))
              for t in reversed(times[-n:]):
                     print(f'{detras}° lugar {t}')
                     detras -= 1
       if opcao == 4:
              print('Em ordem alfabética fica: ')
              for t in sorted(times):
                     print(t)
       if opcao == 5:
              pesquisa=str(input('Digite o nome do Time que deseja buscar: ')).strip()
              print(f'O time {pesquisa} está em {times.index(f"{pesquisa}") + 1}°')

       while True:
              continuar=str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
              if continuar == 'N' or continuar == 'S':
                     break
       if continuar == 'N':
              break
