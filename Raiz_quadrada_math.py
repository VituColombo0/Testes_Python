import math

num = int(input('Escreva um número que você quer ver a raíz quadrada: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {}'.format(num, math.sqrt(num)))


# Podemos chamar a função raiz diretamente da biblioteca math

'''from math import sqrt, floor

num = int(input('Escreva um número que você quer ver a raíz quadrada: '))
raiz = sqrt(num)

print('A raíz quadrada de {} é igual a {}'.format(num, raiz))
print('A raíz quadrada de {} é igual a {}'.format(num, floor(raiz)))'''

# floor arredonda para o número mais próximo
