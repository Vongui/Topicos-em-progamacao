from att_flask_banco.dao.conectar_banco import Banco
from att_flask_venda.model.item_venda import ItemVenda

from att_flask_venda.controller.controller_generico import ControleGenerico


class ControllerItemVenda(ControleGenerico):

    def listarItensPorVenda(self, codvenda):
        self.ob.abrirConexao()
        sql = f"SELECT * FROM item_venda WHERE codvenda = {codvenda}"
        resultado = self.ob.selectQuery(sql)

        lista_itens = []
        for row in resultado:
            item = ItemVenda()
            item.codvenda = row[0]
            item.codproduto = row[1]
            item.qtde = row[2]
            item.valor = row[3]
            lista_itens.append(item)

        return lista_itens
