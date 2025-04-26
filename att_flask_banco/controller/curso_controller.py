from att_flask_banco.controller.generico_controller import ControleGenerico
from att_flask_banco.model.curso import Curso


class CursoController(ControleGenerico):

    def incluir_curso(self, curso):
        self.incluir(curso)

    def alterar_curso(self, curso):
        self.alterar(curso)

    def deletar_curso(self, curso):
        self.delete(curso)

    def pesquisaCodigo(self, entrada: Curso):
        curso = self.procuraRegistro(entrada)
        retorno = Curso()
        if len(curso) >= 1:
            retorno = self.converte_curso(curso)
        return retorno

    def converte_curso(self, curso):
        retorno = Curso()
        retorno.set_idcursos = curso[0][0]
        retorno.set_nomecurso = curso[0][1]
        retorno.set_sigla = curso[0][2]
        return retorno

    def converteObjeto(self, entrada):
        curso = Curso()
        curso.set_idcursos = entrada[0]
        curso.set_nomecurso = entrada[1]
        curso.set_sigla = entrada[2]
        return curso

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        cursos = []
        for registro in registros:
            curso = self.converteObjeto(registro)
            cursos.append(curso)
        return cursos

    def dadosJson(self, dados):
        retorno = {}
        retorno = {
            'idcurso': dados.get_idcursos,
            'nome': dados.get_nomecurso,
            'sigla': dados.get_sigla
        }
        return retorno
