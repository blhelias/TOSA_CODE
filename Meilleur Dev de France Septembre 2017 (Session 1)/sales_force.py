import sys
from typing import List

lines: List = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

L = int(lines[0])
N = int(lines[1])
collab: List = list(map(int, lines[2:]))

etage: int = 0
index: List = []

for count1, equipe1 in enumerate(collab):
    if count1 not in index:
        
        if equipe1 == L:
            etage += 1
            continue
        
        index.append(count1)
        
        for count2 in range(count1, N):
            if ((collab[count2] + equipe1) == L) and (count2 not in index):
                etage += 1
                index.append(count2)
                break

print(etage)
