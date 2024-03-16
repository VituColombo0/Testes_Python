letra = str(input('Insira uma frase:')).upper().strip()

print('A letra "A" aparece {} vezes na frase'.format(letra.count("A")))
print('A primeira letra "A" apareceu na posição {}'.format(letra.rfind('A')))