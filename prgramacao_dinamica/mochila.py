def mochila(pesos, lucros, capacidade):
    n = len(pesos)
    V = [[0 for w in range(capacidade + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] > w:
                V[i][w] = V[i-1][w]
            else:
                V[i][w] = max(V[i-1][w], lucros[i-1] + V[i-1][w - pesos[i-1]])

    return V[n][capacidade], V

# Dados do problema
pesos = [1, 3, 5, 8]
lucros = [1, 5, 8, 10]
capacidade = 11

lucro_max, tabela = mochila(pesos, lucros, capacidade)
print("Lucro máximo:", lucro_max)
