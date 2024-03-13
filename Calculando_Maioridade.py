from datetime import date

atual = date.today().year
maior = 0
menor = 0

for press in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(press)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas de maior e {} de menor'.format(maior, menor))

