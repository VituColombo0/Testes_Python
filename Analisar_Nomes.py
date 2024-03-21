
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))


print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' '))) 
# elimina os espaços entre as palavras

print('Seu primeiro nome é {}, e ele tem {} letras'.format(separa[0], len(separa[0])))
















