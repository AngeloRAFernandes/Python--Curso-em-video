'''Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0

for par in range(1, 7):
    n = int(input('Digite o {}º número: '.format(par)))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você informou {} números PARES e a soma é {}'.format(cont, soma))