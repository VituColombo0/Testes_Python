from random import randint

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Tente adivinhar o número: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente chutar mais alto...')
        elif jogador > computador:
            print('Tente chutar mais baixo...')
print('Acertou com {} palpites'.format(palpites))
#3
