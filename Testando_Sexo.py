sexo = str(input('Insira seu sexo: [M/F] ')).strip().upper()[0] 
# Tira os espaços e joga somente a 1° letra pra maiúsculo

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, insira [M/F] ')).strip().upper()
    [0] # Repetimos aqui pois é um novo input
print('Sexo {} foi registrado'.format(sexo))
