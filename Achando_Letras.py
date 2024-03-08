'''Programa que leia uma frase e:

 Mostre quantas vezes a letra “A” aparece
 A primeira e última vez que ela aparece'''

letra = str(input('Insira uma frase:')).upper().strip()

print('A letra "A" aparece {} vezes na frase'.format(letra.count("A")))
print('A primeira letra "A" apareceu na posição {}'.format(letra.rfind('A')))