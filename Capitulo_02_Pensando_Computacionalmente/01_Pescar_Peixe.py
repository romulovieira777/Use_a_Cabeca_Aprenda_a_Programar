def pescar_peixe():
    print('Pesquei um peixe')


def esperar():
    print('Esperando...')


print('Pegar a minhoca')
print('Colocar a minhoca no anzol')
print('Arremessar a isca')

while True:
    resposta = input('A boia afundou? ')
    if resposta == 'sim':
        esta_movendo = True
        print('Fisguei!')
        pescar_peixe()
    else:
        esperar()
