num = int(input('Insira um número inteiro: '))

print('''Escolha sua opção de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('Você escolheu o número {} que convertido para binário é {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('Você escolheu o número {} que convertido para octal é {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('Você escolheu o número {} que convertido para hexadecimal é {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida.')

# Ele mostra por padrão 2 digítos que mostram o tipo de conversão na frente do número convertido, para tirar isso usamos o [2:]
