def mochila_estudos(pesos, valores, capacidade):
    n = len(pesos)
    V = [[0 for w in range(capacidade + 1)] for i in range(n + 1)]

    # Preenchimento da tabela
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] > w:
                V[i][w] = V[i-1][w]
            else:
                V[i][w] = max(V[i-1][w], valores[i-1] + V[i-1][w - pesos[i-1]])

    # Traceback para descobrir os itens escolhidos
    w = capacidade
    itens_escolhidos = []
    for i in range(n, 0, -1):
        if V[i][w] != V[i-1][w]:
            itens_escolhidos.append(i-1)  # item i foi incluído (índice i-1)
            w -= pesos[i-1]

    return V[n][capacidade], itens_escolhidos[::-1]  # inverter para ordem correta


# Dados
pesos = [3, 4, 2, 5, 1]
valores = [7, 9, 5, 10, 3]
capacidade = 10

lucro_max, itens = mochila_estudos(pesos, valores, capacidade)

# Resultado
print("Importância total máxima:", lucro_max)
print("Itens escolhidos (índice, peso, valor):")
for i in itens:
    print(f"Item {i+1} → peso: {pesos[i]}h, importância: {valores[i]}")