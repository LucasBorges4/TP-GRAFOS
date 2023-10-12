import networkx as nx


def excentricidadeVertice(graph, vertice):
    return nx.eccentricity(graph, v=vertice)