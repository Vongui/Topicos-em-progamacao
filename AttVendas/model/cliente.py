class Cliente:

    def __init__(self):
        self.codcliente = 0
        self.nome = ""
        self.endereco = ""

    def __repr__(self):
        return f"Cliente(codcliente = {self.codcliente}, nome = {self.nome}, endereco = {self.endereco})"
