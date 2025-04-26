class Curso:

    def __init__(self):
        self._idcursos = 0
        self._nomecurso = ""
        self._sigla = ""
        self._lista = 'nomecurso, sigla'

        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = 'cursos'

    @property
    def lista(self):
        return self._lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._nomecurso}','{self._sigla}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (
            "nomecurso='{}', sigla='{}' where idcursos={}").format(self._nomecurso,
                                                     self._sigla,
                                                     self._idcursos)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idcursos={}".format(self._idcursos)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from cursos where idcursos={}".format(self._idcursos)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def get_idcursos(self):
        return self._idcursos

    @property
    def get_nomecurso(self):
        return self._nomecurso

    @property
    def get_sigla(self):
        return self._sigla

    @get_idcursos.setter
    def set_idcursos(self, idcursos):
        self._idcursos = idcursos

    @get_nomecurso.setter
    def set_nomecurso(self, nomecurso):
        self._nomecurso = nomecurso

    @get_sigla.setter
    def set_sigla(self, sigla):
        self._sigla = sigla

    def __str__(self):
        return f'Curso: {self._nomecurso}, Sigla: {self._sigla}'

    def __repr__(self):
        return f'Curso: {self._nomecurso}, Sigla: {self._sigla}'

