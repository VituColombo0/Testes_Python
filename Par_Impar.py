# O resto da divisão % de qualquer número par por 2 sempre é 0, e de qualquer ímpar é 1

num = int(input('Insira qualquer número: '))
resultado = num % 2

if resultado == 0:
    print('\033[31m É um número par \033[m')
else:
    print('\033[36m É um número ímpar \033[m')

