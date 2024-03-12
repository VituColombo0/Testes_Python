produto = float(input('Insira o preço do produto: '))
pag = int(input('Insira a forma de pagamento: \n 1 - À VISTA com dinheiro/cheque \n 2 - À VISTA com cartão \n 3 - 2X NO CARTÃO \n 4 - 3X NO CARTÃO \n Número escolhido:  '))

calc1 = produto - (produto * 0.1)
calc2 = produto - (produto * 0.05)
calc3 = produto
calc4 = produto + (produto * 0.2)


if pag == 1:
    print('Você recebeu 10% de desconto no valor do produto, ficando {}'.format(calc1))
elif pag == 2:
    print('Você recebeu 5% de desconto no valor do produto, ficando {}'.format(calc2))
elif pag == 3:
    print('O preço continua o mesmo')
else:
    print('O valor do produto aumentou em 20%, ficando {}'.format(calc4))
    