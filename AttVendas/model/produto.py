class Produto:

    def __init__(self):
        self.codproduto = 0
        self.nome = ""
        self.preco = 0.0

    def __repr__(self):
        return f"Produto(codproduto = {self.codproduto}, nome = {self.nome}, preco = {self.preco})"
