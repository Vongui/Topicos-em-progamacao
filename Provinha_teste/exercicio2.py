import re
from collections import defaultdict, Counter

def mais_vogais(entrada):
    with open(entrada, 'r') as f:
        palavras = re.findall(r'\b\w+\b', f.read().lower())

    contar = lambda p: sum(1 for l in p if l in 'aeiou')
    max_vogais = max(map(contar, palavras), default=0)
    palavras_vogais = [p for p in set(palavras) if contar(p) == max_vogais]

    print(f"Palavras com {max_vogais} vogais:")
    for i, p in enumerate(palavras_vogais, 1):
        print(f"{i}. {p}")

mais_vogais("entrada.txt")