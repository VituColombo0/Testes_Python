soma = 0
cont = 0

for c in range(1, 501, 2):
    # Se o valor da variável for divisível por 3 sem deixar restos (divisão inteira), a condição é aplicada
    if c % 3 == 0:
        cont += 1 # Outro método
        soma = soma + c  # Soma recebe o que ela tem + c
print('A soma de todos os valores é {} e {} números foram utilizados'.format(soma, cont))
