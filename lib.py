#!/usr/bin/env python3

import networkx as nx
from sys import stderr

def shortest_path(graph, src, dst):
    try:
        if not nx.has_path(graph, src, dst):
            print(f"Distância entre '{src}' e '{dst}' é infinita (sem caminhos)")
            return
        path = nx.shortest_path(graph, src, dst)
        print(f"Distância entre '{src}' e '{dst}' é de: {len(path)}")
        print_path("Caminho mínimo entre eles: ", path)
    except nx.NodeNotFound:
        if src not in graph.nodes:
            print(f"ERRO: o vértice '{src}' não existe", file=stderr)
            return
        print(f"ERRO: o vértice '{dst}' não existe", file=stderr)

def print_path(prompt, path):
    if len(path) == 0: return # não há o que imprimir
    print(f"{prompt}{path[0]}", end="")
    for v in path[1:]:
        print(f" -> {v}", end="")
    print()
