# 3 - Crie uma função chamada filtrar_maioridade(pessoas) que recebe uma lista de
# dicionários, onde cada dicionário contém nome e idade, e retorna uma lista
# apenas com os nomes de quem tem idade maior ou igual a 18.
# [
# {"nome": "Ana", "idade": 20},
# {"nome": "João", "idade": 16}
# ]

pessoas =  [{"nome": "Ana", "idade": 20},{"nome": "João", "idade": 18}]
# print(pessoas['idade'])

def filtrar_maioridade(pessoas):
    lista = []
    for pessoa in pessoas:
        x = pessoa["idade"]
        y = pessoa["nome"]
        if  x >= 18:
            lista.append(y)

    return lista


print(filtrar_maioridade(pessoas))