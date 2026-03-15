# Tabuleiro 4x4
tabuleiro = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]

# Posicao do tesouro
linha_tesouro = 3
coluna_tesouro = 1

def exibe_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('---------')

tentativas = 6

print("MISSAO ESPACIAL - ENCONTRE O METEORITO!")
print("Um meteorito caiu em algum lugar do mapa 4x4.")
print("Voce e o unico astronauta capaz de encontra-lo.")
print("Use numeros de 0 a 3 para linha e coluna.")

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}")
    exibe_tabuleiro()

    linha = int(input("Linha (0 a 3): "))
    coluna = int(input("Coluna (0 a 3): "))

    if linha < 0 or linha > 3 or coluna < 0 or coluna > 3:
        print("Coordenada invalida! Use apenas valores entre 0 e 3.")
        continue

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = 'M'
        print("\nMISSAO CUMPRIDA! Voce encontrou o meteorito!")
        exibe_tabuleiro()
        break
    else:
        if tabuleiro[linha][coluna] != ' ':
            print("Ja vasculhou aqui! Explore outro setor.")
        else:
            tabuleiro[linha][coluna] = '-'
            print("Setor vazio... o meteorito nao esta aqui.")
        exibe_tabuleiro()
else:
    print("\nMISSAO FRACASSADA! O tempo acabou.")
    tabuleiro[linha_tesouro][coluna_tesouro] = 'M'
    print("O meteorito estava aqui:")
    exibe_tabuleiro()