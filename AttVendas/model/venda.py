class Venda:

    def __init__(self):
        self.codvenda = 0
        self.valor_total = 0.0
        self.codcliente = 0
        self.lista_itens = []

    def __repr__(self):
        return f"Venda(codvenda = {self.codvenda}, codcliente = {self.codcliente}, valor total = {self.valor_total})"