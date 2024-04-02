import math

num = float(input('Insira um número quebrado: '))
calc = math.floor(num)

print('O valor {} de forma inteira é {}'.format(num, calc))

# floor arredonda para baixo e ceil para cima

# Sem o uso de bibliotecas:

'''
num = float(input('Insira um número quebrado: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num)))
'''

