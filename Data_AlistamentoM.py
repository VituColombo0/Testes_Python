from datetime import date

ano = int(input('Insira seu ano de nascimento: '))
ano2 = date.today().year

conta = ano2 - ano


if conta == 18:
    print('Você deve se alistar')
elif conta > 18:
    print('Você já passou da idade de se alistar, se passaram {} anos'.format(conta - 18))
else:
    print('Você não precisa se alistar, ainda faltam {} anos'.format(18 - conta))
