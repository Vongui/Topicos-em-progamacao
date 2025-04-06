from aluno import Aluno
from ControllerAluno import Controller

aluno = Aluno()
controlador = Controller(aluno)


def coletar_dados():
    aluno = Aluno()

    print("Digite o nome do aluno: ")
    aluno.nome = input()
    print("Digite o sobrenome: ")
    aluno.sobrenome = input()
    print("Digite a matricula: ")
    aluno.matricula = input()
    controlador.incluir(aluno)

def menu():
    flag = True
    while flag:
        print("\n0 - Sair")
        print("1 - Incluir dados")
        print("2 - Listar dados")
        print("3 - Pesquisar dados")

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue

        if op == 0:
            flag = False
        elif op == 1:
            coletar_dados()
        elif op == 2:
            lista = controlador.listar()
            if lista:
                for x in lista:
                    print(f"Nome: {x[0]} {x[1]}, Matrícula: {x[2]}")
            else:
                    print("Nenhum aluno encontrado")
        elif op == 3:
            print("Digite o Prontuario: ")
            pront = input()
            lista = controlador.pesquisar(pront)
            if lista != None:
                for x in lista:
                    print(f"Nome: {x[0]} {x[1]}, Matricula: {x[2]}")
            else:
                print("Aluno não encontrado")


menu()
