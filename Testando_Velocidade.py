v = float(input('Insira a velocidade do carro: '))
m = (v - 80) * 7

if v > 80:
    print(
        'Você foi multado, e deve pagar 7 reais por Km rodado acima do limite, no caso R${:.2f}'.format(m))
else:
    print('Você não foi multado!')
