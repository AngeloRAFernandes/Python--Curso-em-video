# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quntos km foram percorridos? '))
d = int(input('Quantos dias de aluguel? '))

p = (60 * d) + (0.15 * km)

print('O valor do aluguel a ser pago é R$ {:.2f}'.format(p))
