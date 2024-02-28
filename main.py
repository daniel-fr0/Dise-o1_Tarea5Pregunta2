from hopcroftKarp import *
from esPrimo import esPrimo

C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dado C, se crea un grafo bipartito con los nodos de C
graph = BipGraph(len(C), len(C))
for i in range(len(C)):
	if i % 2 != 0:
		continue
	for j in range(len(C)):
		if j % 2 == 0:
			continue
		if esPrimo(C[i] + C[j]):
			graph.addEdge(i + 1, j + 1)

# Se aplica el algoritmo de Hopcroft-Karp para encontrar el matching
matching = graph.hopcroftKarp()

# Se imprimen los nodos del matching
for i in range(1, len(C) + 1):
	if graph.getPairU()[i] != 0:
		print(C[i - 1], C[graph.getPairU()[i] - 1])
