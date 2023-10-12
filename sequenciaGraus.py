def sequenciaGraus(grafo):
    graus = [grau for vertice, grau in grafo.degree()]
    return graus
