import networkx as nx
from sys import stderr
import matplotlib.pyplot as plt

def checa_conexo(G):
    if G.is_directed() and not nx.is_strongly_connected(G):
        return False
    elif not G.is_directed() and not nx.is_connected(G):
        return False
    return True

def excentricidade(grafo, vertice):
    if not checa_conexo(grafo):
        raise Exception("O grafo não é conexo!")
    excentricidade = nx.eccentricity(grafo, v=vertice, weight="weight")
    return excentricidade

def raio(grafo):
    if not checa_conexo(grafo):
        raise Exception("O grafo não é conexo!")
    raio = nx.radius(grafo, weight="weight")
    return raio

def diametro(grafo):
    if not checa_conexo(grafo):
        raise Exception("O grafo não é conexo!")
    diametro = nx.diameter(grafo, weight="weight")
    return diametro

def centro(grafo):
    if not checa_conexo(grafo):
        raise Exception("O grafo não é conexo!")
    centro = nx.center(grafo, weight="weight")
    return centro

def menor_caminho(G: nx.Graph, orig: str, dest: str):
    try:
        if not nx.has_path(G, orig, dest):
            print(f"Distância entre {orig} e {dest} é infinita")
            return
        dist = nx.shortest_path_length(G, source=orig, target=dest, weight="weight")
        caminho = nx.shortest_path(G, source=orig, target=dest, weight="weight")
        print(f"Distância entre {orig} e {dest} é {dist}")
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
    print("Vértices percorridos na busca em largura, em ordem:")
    for v in nx.topological_sort(AL):
        print(v)
    # Determina as arestas que não fazem parte da árvore de largura
    print("Arestas que não fazem parte da árvore: ", end="")
    for aresta in G.edges():
        if aresta not in AL.edges():
            print(aresta)
    nx.write_graphml(AL, arq)

def centralidade_proximidade(G: nx.Graph, x: str) -> float:
    acc = 0
    for y in G.nodes():
        try:
            dist = nx.shortest_path_length(G, source=x, target=y, weight="weight")
            acc += dist # type: ignore
        except nx.NetworkXNoPath:
            raise Exception(f"Nem todos os outros vértices são alcançáveis de {x}!")
    res = (G.number_of_nodes() - 1) / acc
    return res

def plotar_grafo(G):
    try:
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw(G, pos, with_labels=True, node_size=500)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.title("Grafo")
        plt.show()
    except Exception as e:
        print(f"Erro ao ler o grafo: {e}")

# Heurística de conjunto de estabilidade
def conjunto_estabilidade(G):
    S = []
    # Cria uma lista dos nós ordenados pelo grau (crescente)
    nos = [v for v, _ in sorted(G.degree, key=lambda x: x[1])]
    while len(nos) > 0:
        v = nos.pop() # vértice de maior grau
        S.append(v)
        # Remove tanto o vértice de maior grau quanto os seus vizinhos
        # da lista de nós restantes
        nos = [w for w in nos if w not in G.adj[v]]
    return S

def emparelhamento_maximo(G):
    return nx.max_weight_matching(G)

def verifica_ciclo(G):
    try:
        if G.is_directed():
            cycles = nx.simple_cycles(G)
        else:
            cycles = nx.cycle_basis(G)
        return any(cycles)
    except nx.NetworkXNoCycle:
        return False

def menor_ciclo(G):
    if verifica_ciclo(G):
        
        menor_ciclo = None
        menor_peso = float('inf')
        
        is_ponderado = any('weight' in G[u][v] for u, v in G.edges)
        
        if G.is_directed():
            # Usar find_cycle para grafos direcionados
            for ciclo in nx.simple_cycles(G):
                if is_ponderado:
                    peso_ciclo = sum(G.get_edge_data(u, v)['weight'] for u, v in zip(ciclo, ciclo[1:] + [ciclo[0]]))
                else:
                    peso_ciclo = len(ciclo)
                    
                if peso_ciclo < menor_peso:
                    menor_ciclo = ciclo
                    menor_peso = peso_ciclo
                    
        else:
            # Usar find_cycle para grafos não direcionados
            for ciclo in nx.cycle_basis(G):
                if is_ponderado:
                    peso_ciclo = sum(G.get_edge_data(u, v)['weight'] for u, v in zip(ciclo, ciclo[1:] + [ciclo[0]]))
                else:
                    peso_ciclo = len(ciclo)
                    
                if peso_ciclo < menor_peso:
                    menor_ciclo = ciclo
                    menor_peso = peso_ciclo
                    
        return menor_ciclo, menor_peso
    
    else:
        return None, float('inf')
    
def arvore_geradora_minima(G, arquivo):
    try:
        is_ponderado = any('weight' in G[u][v] for u, v in G.edges)
        
        if G.is_directed():
            if not nx.is_strongly_connected(G):
                raise nx.NetworkXError("O grafo não é fortemente conexo!")
            else:
                agm = nx.minimum_spanning_arborescence(G)
        else:
            agm = nx.minimum_spanning_tree(G)
            
        if not agm.edges:
            raise nx.NetworkXError("O grafo não possui uma árvore geradora mínima!")
        
        if is_ponderado:
            peso_total = sum(G.get_edge_data(u, v)['weight'] for u, v in agm.edges)
        else:
            peso_total = sum(1 for _ in agm.edges)
        
        nx.write_graphml(agm, arquivo)
        
        return peso_total
    
    except nx.NetworkXError as e:
        print(f'Erro: {e}')
        return None
