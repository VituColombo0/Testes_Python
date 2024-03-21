num = int(input('Insira um número de 4 digitos: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))