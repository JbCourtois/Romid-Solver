from collections import defaultdict
from unicodedata import normalize
import json


def capitalize(s):
    return ''.join(c for c in normalize('NFD', s) if c.isalpha()).upper()


words = defaultdict(set)

with open('liste.txt') as file:
    for word in file:
        if '-' in word:
            continue
        word = capitalize(word)
        if not 4 <= len(word) <= 10:
            continue
        words[len(word)].add(word)


for length, wset in words.items():
    wset = list(sorted(wset))
    with open(f'Mots/{length}-full.json', 'w') as file:
        json.dump(wset, file)
