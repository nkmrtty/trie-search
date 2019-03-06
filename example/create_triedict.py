# coding: utf-8
import sys
from marisa_trie import Trie

patterns = []
for line in iter(sys.stdin.readline, ""):
    #if not isinstance(line, unicode):
    #    line = line.decode('utf-8')
    ptn = line.strip().replace('_', ' ').lower()
    if len(line) == 0:
        continue
    patterns.append(ptn)

trie = Trie(patterns)
trie.save('triedict')
