from datetime import date

ano = int(input('Insira seu ano de nascimento: '))
ano2 = date.today().year

idade = ano2 - ano

if idade < 9:
    print('Você faz parte da categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você faz parte da categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você faz parte da categoria JUNIOR')
elif idade == 20:
    print('Você faz parte da categoria SÊNIOR')
else:
    print('Você faz parte da categoria MASTER')