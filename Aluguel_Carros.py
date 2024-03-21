km = float(input('Insira quantos Km foram percorridos: '))
dias = int(input('Insira por quantos dias ele foi alugado: '))

conta1 = km * 0.15
conta2 = dias * 60

print('Você percorreu um total de {}Km e alugou o carro por {} dias \n O preço pela gasolina será de R${} e o do aluguel R${} \n Resultando num total de R${:.2f}'.format(
    km, dias, conta1, conta2, conta1 + conta2))
