from controle import *

def menu():
    controle = Controle()

    while True:
        print("\n--- Menu ---")
        print("1 - Listar todas as conexões")
        print("2 - Filtrar conexões por usuário")
        print("3 - Exibir resumo de acessos por host")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            controle.listar()
        elif opcao == "2":
            user = input("Digite o nome do usuário: ")
            controle.filtrar(user)
        elif opcao == "3":
            for host, dados in controle.resumo().items():
                print(f"host: {host} Qtde acesso: {dados['qtd_acesso']} Usuarios: {dados['usuarios']}")
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

