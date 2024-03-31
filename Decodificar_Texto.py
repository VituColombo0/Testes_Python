"""
Para converter a string para ASCII iremos usar uma propriedade do python que segue a seguinte sintaxe:
(Isso se aplica as linhas 15-34, irei explicar tudo em cima para simplicar o código)

resultado.append(chr(ord(char))

char: Vai pegar o caractere atual que foi digitado

ord(char): Retorna o valor inserido no formato ASCII

chr(...): Converte o valor ASCII de volta para o caractere correspondente

resultado.append(...): Adiciona o caractere que foi alterado à lista resultado.

"""


# Função para codificar uma string recebida pelo usuário
def decodificador(string):

    # Lista para armazenar o resultado final da decodificação
    resultado = []

    # Iteração sobre cada caractere da string recebida
    for char in string:
        # Verifica se o caractere atual é maiúsculo
        if char.isupper():
            # Converte o caractere para o terceiro caractere da ASCII à direita
            resultado.append(chr(ord(char) + 3))
        # Verifica se o caractere atual é minúsculo
        elif char.islower():
            # Converte o caractere para o primeiro caractere da ASCII à esquerda
            resultado.append(chr(ord(char) - 1))
        # Verifica se o caractere é "!"
        elif char == '!':
            # Converte o caractere para o segundo caractere da ASCII à direita
            resultado.append(chr(ord(char) + 2))
        # Verifica se é um caractere especial entre as posições 33 e 125 da ASCII
        elif 33 <= ord(char) <= 125:
            # Converte o caractere para o primeiro caractere da ASCII à esquerda
            resultado.append(chr(ord(char) - 1))
        else:
            # Mantém o caractere original se não se encaixar nas regras anteriores
            resultado.append(char)

    # Retorna o resultado da decodificação como uma lista de caracteres
    return resultado


# Solicita ao usuário uma string para ser codificada
texto = input("Digite um texto para ser codificado: ")

# Chama a função decodificador para decodificar a string recebida
resultado = decodificador(texto)

# Apresenta o resultado final da string codificada ao usuário
print("• O texto inserido decodificado é: ")
print("".join(resultado))
