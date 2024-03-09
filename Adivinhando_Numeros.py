from random import randint

num = (randint(0, 5))
num2 = int(input('Qual número você acha que eu escolhi? '))

if num == num2:
    print('Você acertou!!!')
else:
    print('Você errou!!!')

# Outra maneira:
    
'''from random import choice

escolha = int(input('Que número você acha que eu escolhi? '))
num = [1, 2, 3, 4, 5]
escolhido = choice(num)

print('O número escolhido foi {}'.format(escolhido))

if escolhido == escolha:
    print('Você ACERTOU!!!')
else:
    print('Você ERROU!!!')'''