#exemplo de lambda
import random

quadrado = lambda x : x ** 2
print(quadrado(4))


#exemplo de map
numeros = [1,2,3,4]
dobros = list(map(quadrado, numeros))
print(dobros)

#igual o anterior
# dobros = [x**2 for x in numeros]
# print(dobros)

#reduce
from functools import reduce

numeros = [1,2,3,4]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)

numeros = [3,32,7,5,20,8]
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)
print(max(numeros))

#transposicao
matriz = [[1,2,3], [4,5,6]]
transposta = list(map(list, zip(*matriz)))
print(transposta)


l = []
for x in range(1,21):
    l.append(random.randint(1,100))
multiplos_3 = list(filter(lambda x: x % 3 == 0, l))
print(f"Multiplos de 3: {multiplos_3}")


#ex 2
nomes = ["Ana", "João", "Amanda", "Bruno", "Alana"]
lista = list(filter(lambda x: x[0] == 'A', nomes))
print(lista)

#ex 3
lista = [1,2,3,4,5]
multiplicacao = reduce(lambda x, y: x*y , lista)
print(multiplicacao)