"""
O jogo será reproduzido em um tabuleiro 10x10
Primeiro iremos escolher a linha e depois a coluna, onde os valores variam entre 0-9
O computador possui 5 navios, entre eles:

Porta-aviões 5 casas
Cruzador 4 casas
Contratorpedeiro 3 casas
Rebocador 2 casas
Rebocador_2 2 casas 

Para marcação iremos utilizar:

@ = localização do navio, ela permanece oculta
X = Representação de quando um navio é encontrado e bombardeado
$ = Representação de quando acertamos o tiro na água

"""
import random
# Importamos a biblioteca random para poder usar os termos randint e choice
# Randint = sorteia números, podendo ou não ser em um determinado limite de opções
# Choice = faz a escolha de algum número, podendo ou não ser em um determinado limite de opções

# Função para criar um tabuleiro vazio


def criar_tabuleiro():
    # Criamos uma matriz 10x10 que será preenchida com 'O' para representar a água
    return [['O' for _ in range(10)] for _ in range(10)]

# Função que verifica se uma posição no tabuleiro está livre para colocar um navio


def verificar_posicao_livre(tabuleiro, linha, coluna, tamanho, orientacao):
    # Verifica se a posição está dentro dos limites do tabuleiro
    if orientacao == 'horizontal':
        if coluna + tamanho > 10:
            return False
        # Verifica se as posições necessárias estão livres no eixo X
        return all(tabuleiro[linha][coluna+i] == 'O' for i in range(tamanho))
    elif orientacao == 'vertical':
        if linha + tamanho > 10:
            return False
        # Verifica se as posições necessárias estão livres no eixo Y
        return all(tabuleiro[linha+i][coluna] == 'O' for i in range(tamanho))
    return False

# Função para colocar um navio em uma posição no tabuleiro


def colocar_navio(tabuleiro, linha, coluna, tamanho, orientacao):
    # Coloca o navio no tabuleiro de acordo com a orientação
    if orientacao == 'horizontal':
        for i in range(tamanho):
            # Marca a posição do navio com '@'
            tabuleiro[linha][coluna+i] = '@'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            # Marca a posição do navio com '@'
            tabuleiro[linha+i][coluna] = '@'

# Função para distribuir a frota no tabuleiro


def distribuir_frota(tabuleiro):
    # Lista de tamanhos dos navios
    tamanhos_navios = [5, 4, 3, 2, 2]

    # Orientações possíveis para posicionar os navios
    orientacoes = ['horizontal', 'vertical']

    # Para cada tamanho de navio, escolhe uma posição aleatória e orientação para colocá-lo
    for tamanho_navio in tamanhos_navios:
        while True:
            # Escolhe uma posição aleatória
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            # Escolhe uma orientação aleatória entre as 100 possibilidades
            orientacao = random.choice(orientacoes)

            # Verifica se é possível posicionar o navio na posição escolhida
            if verificar_posicao_livre(tabuleiro, linha, coluna, tamanho_navio, orientacao):
                # Coloca o navio no tabuleiro
                colocar_navio(tabuleiro, linha, coluna,
                              tamanho_navio, orientacao)
                break

# Função para exibir o tabuleiro do jogador


def exibir_tabuleiro_jogador(tabuleiro):
    # Exibe o tabuleiro sem revelar as posições dos navios do computador
    for linha in tabuleiro:
        print(' '.join(linha))

# Função para atirar em uma posição no tabuleiro do computador
def atirar(tabuleiro, linha, coluna):
    # Verifica se o tiro atingiu um navio ou água e atualiza o tabuleiro
    if tabuleiro[linha][coluna] == '@':
        print("Você acertou um navio!")
        tabuleiro[linha][coluna] = 'X'  # Marca o acerto com 'X'
    else:
        print("Tiro na água!")
        tabuleiro[linha][coluna] = '$'  # Marca a água com '$'

# Função para verificar se todos os navios do computador foram afundados
def todos_navios_afundados(tabuleiro):
    # Verifica se ainda há algum navio no tabuleiro do computador
    for linha in tabuleiro:
        if '@' in linha:
            return False
    return True


# Distribuição dos navios e início do jogo
if __name__ == "__main__":
    # Cria tabuleiros para o jogador e o computador
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_adversario = criar_tabuleiro()

    # Distribui a frota no tabuleiro do computador
    distribuir_frota(tabuleiro_adversario)

    # Exibi o tabuleiro do jogador (sem revelar as posições dos navios do computador)
    exibir_tabuleiro_jogador(tabuleiro_jogador)

    # Loop onde ficará repetindo o jogo até que todos os navios sejam encontrados
    while True:
        try:
            # Solicita a entrada de linha e coluna para atirar
            linha = int(input("Escolha a linha para atirar (0-9): "))
            coluna = int(input("Escolha a coluna para atirar (0-9): "))

            # Verifica se a entrada está dentro dos limites do tabuleiro
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print("Entrada inválida. Por favor, escolha valores entre 0 e 9.")
                continue

            # Realiza o tiro no tabuleiro do computador
            atirar(tabuleiro_adversario, linha, coluna)

            # Exibi o tabuleiro do jogador
            exibir_tabuleiro_jogador(tabuleiro_jogador)

            # Exibi o tabuleiro do computador com os tiros
            for linha in tabuleiro_adversario:
                print(' '.join(
                    ['X' if cell == 'X' else '$' if cell == '$' else 'O' for cell in linha]))

            # Verificar se todos os navios do computador foram afundados
            if todos_navios_afundados(tabuleiro_adversario):
                print('Parabéns! Você afundou todos os navios do computador!')
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            # Caso seja inserido algum valor que não esteja nos parâmetros requisitados, a pergunta será feita novamente
