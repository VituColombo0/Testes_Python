num = (int(input('Digite o 1° número: ')),
       int(input('Digite o 2° número: ')),
       int(input('Digite o 3° número: ')),
       int(input('Digite o 4° número: ')),
       int(input('Digite o 5° número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
