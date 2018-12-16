import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

N = int(lines[0]) # nombre de poteaux
poteaux = list(map(int, lines[1:]))

poteaux.sort()
resultat = []

for i in range(N // 2):
    resultat.append(poteaux[i])
    resultat.append(poteaux[(N-1)-i])
    
for i in range(N):
    print(resultat[i], end=" ")
