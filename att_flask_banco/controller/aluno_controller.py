from att_flask_banco.controller.generico_controller import ControleGenerico
from att_flask_banco.model.aluno import Aluno


class AlunoController(ControleGenerico):
    def incluir_aluno(self, aluno):
        self.incluir(aluno)

    def excluir_aluno(self, aluno):
        self.delete(aluno)

    def alterar_aluno(self, aluno):
        self.alterar(aluno)

    def deletar_curso(self, curso):
        self.delete(curso)

    def pesquisaCodigo(self, entrada):
        aluno = self.procuraRegistro(entrada)
        retorno = Aluno()
        if len(aluno) >= 1:
            retorno = self.converte_aluno(aluno)
        return retorno

    def converte_aluno(self, aluno):
        retorno = Aluno()
        retorno.set_idalunos = aluno[0][0]
        retorno.set_alunoscol = aluno[0][1]
        retorno.set_nome = aluno[0][2]
        retorno.set_cidade = aluno[0][3]
        retorno.set_uf = aluno[0][4]
        retorno.set_cep = aluno[0][5]
        retorno.set_email = aluno[0][6]
        retorno.set_prontuario = aluno[0][7]
        retorno.set_idcurso = aluno[0][8]
        return retorno

    def converteObjeto(self, entrada):
        aluno = Aluno()
        aluno.set_idalunos = entrada[0]
        aluno.set_alunoscol = entrada[1]
        aluno.set_nome = entrada[2]
        aluno.set_cidade = entrada[3]
        aluno.set_uf = entrada[4]
        aluno.set_cep = entrada[5]
        aluno.set_email = entrada[6]
        aluno.set_prontuario = entrada[7]
        aluno.set_idcurso = entrada[8]
        return aluno

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        alunos = []
        for registro in registros:
            aluno = self.converteObjeto(registro)
            alunos.append(aluno)
        return alunos

    def dadosJson(self, dados):
        retorno = {}
        retorno = {'idalunos': dados.get_idalunos,
                   'alunoscol': dados.get_alunoscol,
                   'nome': dados.get_nome,
                   'cidade': dados.get_cidade,
                   'uf': dados.get_uf,
                   'cep': dados.get_cep,
                   'email': dados.get_email,
                   'prontuario': dados.get_prontuario,
                   'idcurso': dados.get_idcurso}
        return retorno