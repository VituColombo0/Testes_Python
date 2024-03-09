s = float(input('Qual o seu salário? '))
a1 = s * 0.1
a2 = s * 0.15

if s >= 1250.00:
    print('Você recebeu um aumento de R${:.2f} e seu novo salário é de R${}'.format(a1, s + a1))
else:
    print('Você recebeu um aumento de R${:.2f} e seu novo salário é de R${}'.format(a2, s + a2))
    