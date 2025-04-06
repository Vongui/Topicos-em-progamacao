class Aluno:

    def __init__(self, nome = " ", sobrenome = " ", matricula = " "):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula

    @property
    def get_nome(self):
        return self.nome

    @property
    def get_sobrenome(self):
        return self.sobrenome

    @property
    def get_matricula(self):
        return self.matricula

    @property
    def set_nome(self, nome = " "):
        self.nome = nome

    @property
    def set_sobrenome(self, sobrenome=" "):
        self.sobrenome = sobrenome

    @property
    def set_matricula(self, matricula=" "):
        self.matricula = matricula

