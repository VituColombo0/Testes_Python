resp = 'S'
soma = media = quant = 0
# Inicializar essas variáveis com 0 garante que elas existam 
# E têm um valor inicial válido antes de serem usadas dentro do loop. 

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
#