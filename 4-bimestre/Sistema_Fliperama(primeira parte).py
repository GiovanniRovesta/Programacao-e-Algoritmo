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


def main():

    while True:
        option = input("Escolha uma opção: ")

        if option == "1":
            cadastrar_usuario()
        elif option == "2":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                comprar_tokens(usuario_atual)
        elif option == "3":
            quantidade_tokens()
        elif option == "4":
            horas_jogaveis()
        elif option == "5":
            saldo_total()
        elif option == "6":
            jogos_disponiveis()
        elif option == "7":
            save_data()
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


main()
