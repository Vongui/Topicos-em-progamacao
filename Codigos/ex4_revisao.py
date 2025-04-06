# 4 - Dado um arquivo vendas.csv no seguinte formato:
# produto,quantidade,preco_unitario
#     Mouse,3,50
#     Teclado,2,100
#     Mouse,1,50
# Crie uma função que:
#         • Leia o arquivo.
#         • Calcule o total vendido por produto.
#         • Retorne um dicionário com o nome do produto e o valor total das vendas.
# Resultado esperado
# {"Mouse": 200, "Teclado": 200}

def calcular_total_vendas():
    vendas_por_produto = {}

    with open("vendas", 'r') as arquivo:
        dados = arquivo.readlines()

        for linha in dados:
            produto, quantidade, preco = linha.strip().split(';')

            quantidade = int(quantidade)
            preco = float(preco)

            total_da_linha = quantidade * preco

            if produto in vendas_por_produto:
                vendas_por_produto[produto] += total_da_linha
            else:
                vendas_por_produto[produto] = total_da_linha

    return vendas_por_produto


resultado = calcular_total_vendas()
print(resultado)


