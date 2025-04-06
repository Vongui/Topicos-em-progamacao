class Conexao:

    def __init__(self):
        self.id = ""
        self.hora = ""
        self.host = ""
        self.porta = ""
        self.usuario = ""
        self.database = ""

    def get_id(self):
        return self.id

    def get_hora(self):
        return self.hora

    def get_host(self):
        return self.host

    def get_porta(self):
        return self.porta

    def get_usuario(self):
        return self.usuario

    def get_database(self):
        return self.database

    def set_id(self, id):
        self.id = id

    def set_hora(self, hora):
        self.hora = hora

    def set_host(self, host):
        self.host = host

    def set_porta(self, porta):
        self.porta = porta

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_database(self, database):
        self.database = database
        
    def __repr__(self):
        return f"Id: {self.id}, hora: {self.hora}, host: {self.host}, porta: {self.porta}, usuario: {self.usuario}, database: {self.database}"
