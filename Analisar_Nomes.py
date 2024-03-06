'''Programa que leia o nome completo e mostre:

- Nome todo em maiúsculo/minúsculo
- Quantas letras ao todo, tirando todos os espaços
- Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))

print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome é {}, e ele tem {} letras'.format(separa[0] , len(separa[0])))

