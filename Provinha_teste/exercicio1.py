import re
from collections import Counter

def processar_arquivo(entrada, saida):
    with open(entrada, 'r', encoding="utf-8" ) as f:
        texto = f.read().lower()

    palavras = re.findall(r'\b\w+\b', texto)
    contagem = Counter(palavras)

    maior = max(palavras, key=len)
    menor = min(palavras, key=len)
    repetidas = {p: c for p, c in contagem.items() if c > 1}
    resumo = Counter(len(p) for p in palavras)

    with open(saida, 'w', encoding="utf-8") as f:
        for i, linha in enumerate(texto.split('\n'), 1):
            f.write(f"{i:04} {linha}\n")
        f.write(f"Maior palavra: {maior}\nMenor palavra: {menor}\n")
        f.write("Palavras repetidas:\n" + '\n'.join(f"{p} => {c}" for p, c in repetidas.items()) + '\n')
        f.write("Resumo:\n" + '\n'.join(f"Com {t} letras = {c}" for t, c in sorted(resumo.items())))

processar_arquivo("entrada.txt", "saida.txt")