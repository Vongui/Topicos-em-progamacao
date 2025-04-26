def troco(moedas, n, m):
    if n == 0:
        return 1
    if n < 0 or m <= 0:
        return 0
    return troco(moedas, n - moedas[m - 1], m) + troco(moedas, n, m - 1)

moedas = [1, 2, 5]
n = 5
m = len(moedas)
print(troco(moedas, n, m))