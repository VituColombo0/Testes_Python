# Os valores estipulados foram os mesmos do exercício

# Criamos uma função para compactar um vetor
def compactacao(vetor):
    # Inicializamos uma lista para armazenar a compactação
    comprimido = []
    # Inicializamos um contador para contar a frequência de cada número
    contador = 1

    # Repetimos cada elemento do vetor, exceto o primeiro
    for i in range(1, len(vetor)):
        # Verificamos se o elemento atual é igual ao anterior
        if vetor[i] == vetor[i - 1]:
            # Incrementamos o contador de frequência se for igual ao anterior
            contador += 1
        else:
            # Adicionamos o elemento anterior e quantas vezes ele aparece à lista de compactação
            comprimido.append((vetor[i - 1], contador))
            # Reiniciamos o contador para o próximo número
            contador = 1

    # Adicionamos o último elemento do vetor e quantas vezes ele aparece à lista de compactação
    comprimido.append((vetor[-1], contador))

    # Retornamos a lista de compactação
    return comprimido


# Definimos os valores do vetor
vetor = [30, 30, 30, 8, 8, 30, 5, 5, 5, 5, 20, 20, 6, 6, 6]

# Chamando a função para compactar o vetor original
resultado = compactacao(vetor)

# Exibimos os valores que foram já escolhidos
print("• O vetor original é:", vetor)

# Exibimos os valores de forma compactada, como mostrado no exemplo da Figura2
print("• O vetor compactado é:", [(elemento, contador)
      for elemento, contador in resultado])
