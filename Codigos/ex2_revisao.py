# 2 - Implemente uma classe Produto com os atributos: nome, preco e estoque. A
# classe deve:
# • Ter um método __str__ para retornar a string: "Produto: <nome>,
# R$<preco>, Estoque: <estoque>".
# • Ter um método vender(qtd) que diminui o estoque e retorna o valor total da
# venda.
# • Proibir a venda se o estoque for insuficiente.

class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.estoque = 0

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_estoque(self):
        return self.estoque

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_estoque(self, estoque):
        self.estoque = estoque

    def vender(self, qtd):
        if qtd > self.estoque:
            return -1
        else:
            self.estoque = self.estoque - qtd
            return qtd * self.preco

    def __str__(self):
        return f"Produto: {self.nome}, R${self.preco}, Estoque: {self.estoque}"