import networkx as nx

def excentricidade_Do_Vertice(grafo, vertice):
    excentricidade_Do_Vertice = nx.eccentricity(grafo, v=vertice)
    return excentricidade_Do_Vertice

def raio_Do_Grafo(grafo):
    raio_Do_Grafo = nx.radius(grafo)
    return raio_Do_Grafo

def diametro_Do_Grafo(grafo):
    diametro_Do_Grafo = nx.diameter(grafo)
    return diametro_Do_Grafo

def centro_Do_Grafo(grafo):
    centro_Do_Grafo = nx.center(grafo)
    return centro_Do_Grafo
