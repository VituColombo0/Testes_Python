n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO!')
elif media > 5 and media < 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')