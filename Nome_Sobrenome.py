nome = str(input('Digite seu nome: ')).strip()
n = nome.split()

print('Seu primeiro nome é {} e seu sobrenome é {} {}'.format(n[0], n[1], n[2]))