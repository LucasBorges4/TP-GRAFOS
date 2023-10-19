#!/usr/bin/env python3

import networkx as nx
from sys import stderr

def excentricidade(grafo, vertice):
    excentricidade = nx.eccentricity(grafo, v=vertice)
    return excentricidade

def raio(grafo):
    raio = nx.radius(grafo)
    return raio

def diametro(grafo):
    diametro = nx.diameter(grafo)
    return diametro

def centro(grafo):
    centro = nx.center(grafo)
    return centro

def menor_caminho(G: nx.Graph, orig: str, dest: str):
    try:
        if not nx.has_path(G, orig, dest):
            print(f"Distância entre {orig} e {dest} é infinita")
            return
        caminho = nx.shortest_path(G, source=orig, target=dest)
        print(f"Distância entre {orig} e {dest} é {len(caminho)}")
        exibe_caminho("Caminho mínimo:", caminho)
    except nx.NodeNotFound:
        if orig not in G.nodes:
            print(f"ERRO: o vértice '{orig}' não existe", file=stderr)
            return
        print(f"ERRO: o vértice '{dest}' não existe", file=stderr)

def exibe_caminho(nome: str, caminho):
    if len(caminho) == 0: return # não há o que imprimir
    print(f"{nome} {caminho[0]}", end="")
    for v in caminho[1:]:
        print(f" -> {v}", end="")
    print()

def busca_largura(G: nx.Graph, orig: str, arq: str):
    AL = nx.bfs_tree(G, orig)
    # Determina ordem de vértices percorridos
    for v in nx.topological_sort(AL):
        print(v)
    # Determina as arestas que não fazem parte da árvore de largura
    for aresta in G.edges():
        if aresta not in AL.edges():
            print(aresta)
    nx.write_graphml(AL, arq)

def centralidade_proximidade(G: nx.Graph, x: str) -> float:
    acc = 0
    for y in G.nodes():
        dist = nx.shortest_path_length(G, source=x, target=y)
        acc += dist # type: ignore
    res = (G.number_of_nodes() - 1) / acc
    return res
