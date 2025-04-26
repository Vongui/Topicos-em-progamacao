class Aluno:
    def __init__(self):
        self._idalunos = 0
        self._alunoscol = ""
        self._nome = ""
        self._cidade = ""
        self._uf = ""
        self._cep = ""
        self._email = ""
        self._prontuario = ""
        self._curso_idcursos = 0
        self._lista = 'alunoscol, nome, cidade, uf, cep, email, prontuario, curso_idcursos'

        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = 'alunos'

    @property
    def lista(self):
        return self._lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._alunoscol}','{self._nome}','{self._cidade}','{self._uf}','{self._cep}','{self._email}','{self._prontuario}',{self._curso_idcursos}"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (
            "alunoscol='{}', nome='{}', cidade='{}', uf='{}', cep='{}', email='{}', prontuario='{}', curso_idcursos={} where idalunos={}").format(
            self._alunoscol, self._nome, self._cidade, self._uf, self._cep, self._email, self._prontuario, self._curso_idcursos, self._idalunos)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idalunos={}".format(self._idalunos)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from alunos where idalunos={}".format(self._idalunos)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def get_idalunos(self):
        return self._idalunos

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_idcursos(self):
        return self._curso_idcursos

    @property
    def get_alunoscol(self):
        return self._alunoscol

    @property
    def get_cidade(self):
        return self._cidade

    @property
    def get_uf(self):
        return self._uf

    @property
    def get_cep(self):
        return self._cep

    @property
    def get_email(self):
        return self._email

    @property
    def get_prontuario(self):
        return self._prontuario

    @get_idalunos.setter
    def set_idalunos(self, idalunos):
        self._idalunos = idalunos

    @get_nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @get_idcursos.setter
    def set_idcurso(self, idcurso):
        self._curso_idcursos = idcurso

    @get_alunoscol.setter
    def set_alunoscol(self, alunoscol):
        self._alunoscol = alunoscol

    @get_cidade.setter
    def set_cidade(self, cidade):
        self._cidade = cidade

    @get_uf.setter
    def set_uf(self, uf):
        self._uf = uf

    @get_cep.setter
    def set_cep(self, cep):
        self._cep = cep

    @get_email.setter
    def set_email(self, email):
        self._email = email

    @get_prontuario.setter
    def set_prontuario(self, prontuario):
        self._prontuario = prontuario

    def __str__(self):
        return (f"Aluno: {self._alunoscol}, Nome: {self._nome}, Cidade: {self._cidade}, UF: {self._uf}, CEP: {self._cep},"
                f" Email: {self._email}, Prontuário: {self._prontuario}, Curso ID: {self._curso_idcursos}")

    def __repr__(self):
        return (f"Aluno: {self._alunoscol}, Nome: {self._nome}, Cidade: {self._cidade}, UF: {self._uf}, CEP: {self._cep},"
                f" Email: {self._email}, Prontuário: {self._prontuario}, Curso ID: {self._curso_idcursos}")