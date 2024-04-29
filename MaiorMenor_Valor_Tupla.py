from random import randint

num = (randint(0, 5), randint(0, 5), randint(
    0, 5), randint(0, 5), randint(0, 5))
# Como colocamos dentro de () criamos uma tupla para a variável num
print(f'Os valores sorteados foram: {num} \n')
print(f'O maior valor é {max(num)} e o menor valor é {min(num)}')