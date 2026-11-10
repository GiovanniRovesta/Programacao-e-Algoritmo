import json
import os

DATA_FILE = "fliperama_dados.json"

pessoas = []
usuario_atual = None

def load_data():
    global pessoas, usuario_atual

    if not os.path.exists(DATA_FILE):
        pessoas = []
        return

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        pessoas = data.get("pessoas", [])


def save_data():
    data = {
        "pessoas": pessoas
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


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

    save_data()

    print("Você foi cadastrado, pode prosseguir")
    print("Compre os tokens com esse dinheiro!")

def adicionar_dinheiro(pessoa):
    dinheiro = float(input("Quantidade de dinheiro que deseja adicionar: "))
    if dinheiro <= 0:
        print("Você realizou uma ação inválida, adicione dinheiro")
        return
    
    pessoa['dinheiro'] += dinheiro

    save_data()

    print(f"Você adicionou {dinheiro}, seu saldo total é de {pessoa['dinheiro']}")

def comprar_tokens(pessoa):
    token = int(input("Quantos tokens você quer comprar? "))
    if pessoa["dinheiro"] >= 2 * token:
        pessoa["dinheiro"] -= 2 * token
        pessoa["tokens"] += token

        save_data()

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

    horas_desejadas = int(input("Por quantas horas você deseja jogar? "))
    tokens_necessarios = horas_desejadas * 2

    if horas_desejadas > 0 and pessoa["tokens"] >= tokens_necessarios:
        pessoa["tokens"] -= tokens_necessarios
        pessoa["horas"] += horas_desejadas

        save_data()

        print(f"Pode se divertir no {nome} por {horas_desejadas} hora(s)! Você ainda tem {pessoa['tokens']} tokens para gastar")
    else:
        print("Resultado inválido ou tokens insuficientes para essa quantidade de horas.")

def saldo_total(pessoa):
    print(pessoa)

def show_menu():
    print("\n=== Sistema Fliperama ===")
    print("1 - Cadastrar Usuário")
    print("2 - Adicionar Dinheiro")
    print("3 - Comprar Tokens")
    print("4 - Quantidade de Tokens")
    print("5 - Horas Jogaveis")
    print("6 - Jogos Disponiveis")
    print("7 - Saldo Total")
    print("8 - Sair")

def main():

    load_data()

    global usuario_atual
    if len(pessoas) > 0:
        usuario_atual = pessoas[-1] 

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            cadastrar_usuario()
        elif option == "2":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                adicionar_dinheiro(usuario_atual)
        elif option == "3":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                comprar_tokens(usuario_atual)
        elif option == "4":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                quantidade_tokens(usuario_atual)
        elif option == "5":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                horas_jogaveis(usuario_atual)
        elif option == "6":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                jogos_disponiveis(usuario_atual)
        elif option == "7":
            if usuario_atual is None:
                print("Cadastre-se primeiro.")
            else:
                saldo_total(usuario_atual)
        elif option == "8":
            print("Você saiu com êxito")
            break
        else:
            print("Opção inválida.")


main()
