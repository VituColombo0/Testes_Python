# Programa que leia o nome de uma pessoa e verifique se possui “Colombo” no nome

nome = str(input('Insira seu nome completo: ')).strip().upper()

print(nome[0:5] == "COLOMBO")
print(nome[0:5])

