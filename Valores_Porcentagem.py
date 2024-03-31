s = float(input('Insira seu salário: '))
p = float(input('Insira o preço do produto que deseja comprar em R$ '))

conta1 = s * 0.15
valor1 = s + conta1

conta2 = p * 0.05
valor2 = p - conta2

print('Seu antigo salário era de {} agora com o aumento passou a ser {} \n Já o produto com 5% de desconto reduz seu valor em R${}, e seu novo preço se torna R$ {} '.format(s, valor1, conta2, valor2))
