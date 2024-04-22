n1 = int(input('Insira o 1° número: '))
n2 = int(input('Insira o 2° número: '))
menu = 0

while menu != 5:
    menu = int(input('''Insira o que deseja fazer com os valores: \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA \n Inserir: '''))
    if menu == 1:
        print('A soma dos valores é {}'.format(n1 + n2))
    elif menu == 2:
        print('A multiplicação dos valores é {}'.format(n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('{} é o maior valor'.format(n1))
        else:
            print('{} é o maior valor'.format(n2))
    elif menu == 4:
        n1 = int(input('Insira o 1° número: '))
        n2 = int(input('Insira o 2° número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
print('Programa encerrado.')
#