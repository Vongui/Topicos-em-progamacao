class ItemVenda:

    def __init__(self):
        self.codvenda = 0
        self.codprodutp = 0
        self.qtd = 0
        self.valor = 0.0

    def __repr__(self):
        return f"ItemVenda(codproduto = {self.codproduto}, codvenda = {self.codvenda}, valor = {self.valor}, quantidade = {self.qtd})"