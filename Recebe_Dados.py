nome = str(input('Insira seu nome completo: '))
idade = int(input('Insira sua idade: '))
cidade = str(input('Insira sua cidade natal: '))

print('Você se chama \033[31m{},\033[m tem \033[36m{}\033[m anos e nasceu em {}'.format(nome, idade, cidade))
print(f'Você se chama \033[31m{nome} \033[m tem {idade} anos e nasceu em {cidade}')