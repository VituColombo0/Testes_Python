km = float(input('Insira quantos Kms foram percorridos: '))


if km <= 200:
    print('O preço total da viagem ficou em R${}'.format(km * 0.50))
else:
    print('O preço total da viagem ficou em R${}'.format(km * 0.45))
