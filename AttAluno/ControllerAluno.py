from aluno import Aluno

class Controller:
    def __init__(self, aluno=None):
        self.aluno = aluno

    def incluir(self,aluno):
            with open("/home/aluno/Documentos/Alunos.txt", "a") as arquivo:
                arquivo.write(aluno.nome + "/" + aluno.sobrenome + "/" + aluno.matricula + "\n")

    def listar(self):
        with open("/home/aluno/Documentos/Alunos.txt", "r") as arquivo:
            dados_alunos = []
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split("/")
                dados_alunos.append([dados[0], dados[1], dados[2]])
            return dados_alunos

    def pesquisar(self, prontuario):
        with open("/home/aluno/Documentos/Alunos.txt", "r") as arquivo:
            dados_aluno = []
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split("/")
                if dados[2] == prontuario:
                    dados_aluno.append([dados[0], dados[1], dados[2]])
                    return dados_aluno
            return None