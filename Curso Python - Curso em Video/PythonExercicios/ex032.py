'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))

#puxar ano atual do computador
if ano == 0:
    ano = date.today().year

#validação de ano bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
