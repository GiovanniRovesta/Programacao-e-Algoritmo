pessoas = []
usuario_atual = None


def cadastrar_usuario():
    global usuario_atual

    usuario = input("Coloque seu nome: ")
    idade = int(input("Coloque sua idade: "))
    if idade <= 12:
        print("Você é novo demais, procure seus responsáveis")
        return

    dinheiro = float(input("Coloque seu dinheiro: "))
    if dinheiro <= 0:
        print("Quantidade inválida")
        return

    pessoa = {
        "usuario": usuario,
        "idade": idade,
        "dinheiro": dinheiro,
        "tokens": 0,
        "horas": 0
    }

    pessoas.append(pessoa)
    usuario_atual = pessoa

    print("Você foi cadastrado, pode prosseguir")
    print("Compre os tokens com esse dinheiro!")


def comprar_tokens(pessoa):
    token = int(input("Quantos tokens você quer comprar? "))
    if pessoa["dinheiro"] >= 2 * token:
        pessoa["dinheiro"] -= 2 * token
        pessoa["tokens"] += token
        print("Você comprou tokens!")
    else:
        print("Você não tem dinheiro para comprar essa quantidade")

def quantidade_tokens(pessoa):
    print(f"Você tem {pessoa['tokens']} tokens")


def horas_jogaveis(pessoa):
    horas = pessoa["tokens"] // 2
    print(f"Você tem {horas} hora(s) para jogar")

jogos = {
    "1": ("Fliperama", 2),
    "2": ("Dance Games", 3),
    "3": ("Pinball", 3),
    "4": ("Consoles", 5),
}


def jogos_disponiveis(pessoa):
    print("\n=== Jogos do Estabelecimento ===")
    for numero, (nome, custo) in jogos.items():
        print(f"{numero} - {nome} ({custo} tokens)")
    print("5 - Sair")

    escolha = input("Escolha um jogo: ")

    if escolha == "5":
        return

    if escolha not in jogos:
        print("Opção inválida.")
        return

    nome, custo = jogos[escolha]

    if pessoa["tokens"] < custo:
        print("Você não tem tokens suficientes.")
        return

    pessoa["tokens"] -= custo
    print(f"Pode se divertir no {nome}! Você ainda tem {pessoa['tokens']} tokens para gastar")


def show_menu():
    print("\n=== Sistema Fliperama ===")
    print("1 - Cadastrar Usuário")
    print("2 - Comprar Tokens")
    print("3 - Quantidade de Tokens")
    print("4 - Horas Jogaveis")
    print("5 - Jogos Disponiveis")
    print("6 - Saldo Total")
    print("7 - Sair")

def main():

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            cadastrar_usuario()
        elif option == "2":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                comprar_tokens(usuario_atual)
        elif option == "3":
            quantidade_tokens(usuario_atual)
        elif option == "4":
            horas_jogaveis(usuario_atual)
        elif option == "5":
            jogos_disponiveis(usuario_atual)
        else:
            print("Opção inválida.")


main()
