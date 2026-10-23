pessoas = []
tokens = []
dinheiro = []
horas = []

def cadastrar_usuario():
    usuario = input("Coloque seu nome: ")
    idade = int(input("Coloque sua idade: "))
    if idade <= 12:
        print("Você é novo demais, procure seus responsáveis")
        return

    pessoas.append(pessoa)
    print("Você foi cadastrado, pode prosseguir")

    dinheiro = float(input("Coloque seu dinheiro: "))
    if dinheiro > 0:
        print("Compre os tokens com esse dinheiro!")
    else:
        print("Quantidade inválida")

    pessoa = {
        "usuario": usuario,
        "idade": idade,
        "dinheiro": dinheiro
    }

def comprar_tokens():
    token = int(input("Quantos tokens você quer comprar? "))
    if dinheiro >= 2*token:
        print("Você comprou tokens!")
        saldo = pessoas['dinheiro'] - 2*token
    else:
        print("Você não tem dinheiro para comprar essa quantidade")
    


def main():
    load_data()

    while True:
        mostrar_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            cadastrar_usuario()
        elif option == "2":
            comprar_tokens()
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
