import sys

### VENTE AUX ENCHERES ###

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

N = int(lines[0]) # nombre d'enchères recues
P = int(lines[1]) # prix de reserve
encheres = lines[2:]

gagnant = None
prix_gagnant = P
for element in encheres:
    enchere = element.split(" ")
    prix = int(enchere[0])
    user = enchere[1]
    if prix > prix_gagnant:
        prix_gagnant = prix
        gagnant = user

print(prix_gagnant)

### MOT MAGIQUE ###

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

voyelle = [97, 101, 105, 111, 117, 121]

N = int(lines[0])
list_magic = lines[1:]
resultat = []
for _, word in enumerate(list_magic):
    if len(word) >= 5 and len(word) <= 7:
        char1 = word[0]
        char2 = word[1]
        char_end = word[len(word)-1]
        if ord(char2) - ord(char1) == 1:
            if ord(char_end) in voyelle:
                resultat.append(word)

print(len(set(resultat)))

### FONCTION MYSTERIEUSE ###
# TODO: concours
