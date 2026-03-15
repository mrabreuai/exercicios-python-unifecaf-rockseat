print("Sou o Oraculo da Sabedoria Python. Faca sua pergunta...")

pergunta = input("Voce quer saber sobre (funcoes, loops, variaveis, listas)? ")

match pergunta:
    case "funcoes" | "funcao" | "funcao":
        print("Funcoes sao blocos de codigo que voce pode reutilizar! def nome():")
    case "loops":
        print("Loops permitem repetir acoes. Use for ou while!")
    case "variaveis":
        print("Variaveis guardam valores. Exemplo: idade = 18")
    case "listas":
        print("Listas guardam varios valores. Ex: frutas = [maca, banana]")
    case _:
        print("Essa resposta esta alem do meu conhecimento atual.")