num1 = int(input('Insira o 1° número: '))
num2 = int(input('Insira o 2° número: '))

if num1 > num2:
    print('{} é o maior valor'.format(num1))
elif num1 == num2:
    print('Os dois números possuem o mesmo valor') 
else:
    print('{} é o maior valor'.format(num2))#