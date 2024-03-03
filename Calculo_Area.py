# calcular a área da parede, considerando que cada litro de tinta pinta uma área de 2m²

larg = float(input('Insira a largura: '))
alt = float(input('Insira a altura: '))
area = larg * alt
tinta = area / 2

print('A parede tem a dimensão de {}X{} e possui uma área de {}m², para pintá-la irá gastar um total de {}L'.format(larg, alt, area, tinta))