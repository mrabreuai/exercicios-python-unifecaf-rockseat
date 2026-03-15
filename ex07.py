numero_secreto = 7
tentativas = 0

while True:
    chute = int(input("Adivinhe o numero (entre 1 e 10): "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabens! Voce acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente!")