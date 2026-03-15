perguntas = [
    ["Qual e a extensao de um arquivo Python? ", "py"],
    ["Qual comando exibe texto no terminal em Python? ", "print"],
    ["Quantas combinacoes tem uma tabela verdade com 2 variaveis? ", "4"],
    ["Qual simbolo representa o conectivo E na logica? ", "^"],
    ["Como se chama o modelo entrada, processamento e saida? ", "ipo"]
]

acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0])
    if resposta.lower() == pergunta[1]:
        acertos += 1

print(f"Voce acertou {acertos} de {len(perguntas)} perguntas!")