a = input('Insira um texto: ')

print(type(a))

print('Só tem espaços?', a.isspace())

print('É um número?', a.isnumeric())

print('É alfabético?', a.isalpha())

print('É alfanumérico?', a.isalnum())

print('Está em maiúsculo?', a.isupper())

print('Está em minúsculo?', a.islower())

print('Está capitalizada?', a.istitle())
