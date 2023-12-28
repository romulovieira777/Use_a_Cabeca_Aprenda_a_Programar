import random


clientes = ['Jimmy', 'Kim', 'John', 'Stacie']

vencedor = random.choice(clientes)

sabor = 'baunilha'

print('Parabéns ' + vencedor + ' você ganhou um sundae!')

prompt = 'Você quer uma cereja em cima? '

quer_cereja = input(prompt)

pedido = 'sundae de ' + sabor

if (quer_cereja == 'sim'):
    pedido = pedido + ' com uma cereja em cima'

print('Um ' + pedido + ' para ' + vencedor + ' saindo...')
