def classificar_palavras_por_tamanho(entrada, saida):
    with open(entrada, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(saida, 'w', encoding='utf-8') as f:
        for linha in linhas:
            palavras = linha.strip().split()
            palavras_ordenadas = sorted(palavras, key=len)
            f.write('|' + '|'.join(palavras_ordenadas) + '|\n')

classificar_palavras_por_tamanho("entrada.txt", "saida3.txt")