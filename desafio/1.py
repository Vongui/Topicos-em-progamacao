with open("ALEATORIO.TXT", "r") as arquivo:
    linhas = arquivo.readlines()
    dados = []
    for linha in linhas:
        num = linha.strip()
        dados.append(num)



print(dados)
dictio = {}
for x in dados:
    if x in dictio.keys():
        dictio[x]+=1
    else:
        dictio[x]=1
print(dictio)
#
# dicionario_ordenado = sorted(dictio.items(), key=lambda item: item[1], reverse=True)
# print(dicionario_ordenado)