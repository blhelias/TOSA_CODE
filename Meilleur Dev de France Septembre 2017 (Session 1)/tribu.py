import sys
from typing import Dict

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def compte_soldats(self, idx):
        # recursively navigate through the tribu and count wariors
        if self.graph[idx]["scratch"]:
            return 0
        # mark the clan as visited
        self.graph[idx]["scratch"] = True
        # check if the clan has friends and iterate over the friends
        if self.graph[idx]["vassals"]:
            for voisins in self.graph[idx]["vassals"]:
                self.graph[idx]["total"] += self.compte_soldats(voisins)

        return self.graph[idx]["total"]

    def reset_graph(self):
        for key, _ in self.graph.items():
            self.graph[key]["scratch"] = False
            self.graph[key]["total"] = self.graph[key]["nb_soldats"]

lines = []
for line in sys.stdin:
	    lines.append(line.rstrip('\n').split(" "))

n_tribu = lines[0]
resultats = []
tribu: Dict = {}
# build tribu network / graph
for i in range(1, len(lines)):
    element = i-1
    tribu[element] = {}
    tribu[element]["nb_soldats"] = int(lines[i][0])
    tribu[element]["vassals"] = list(map(int, lines[i][1:]))
    tribu[element]["total"] = int(lines[i][0]) # make the sum of all the allies
    tribu[element]["scratch"] = False # by default the clan is not marked as visited

gr = Graph(tribu)
for tribu_idx, _ in gr.graph.items():
    resultats.append(gr.compte_soldats(tribu_idx))
    gr.reset_graph()
    
print("reponse = ", max(resultats))