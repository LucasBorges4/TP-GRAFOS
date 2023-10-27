import networkx as nx
import lib, graph

def remover_vertice(G: nx.Graph, vertice: str):
    if vertice in G.nodes:
        G.remove_node(vertice)
        print(f"Vértice {vertice} removido com sucesso.")
    else:
        print(f"Vértice {vertice} não encontrado no grafo.")

def adicionar_aresta(G: nx.Graph, origem: str, destino: str, peso: float):
    if origem in G.nodes and destino in G.nodes:
        G.add_edge(origem, destino, weight=peso)
        print(f"Aresta ({origem}, {destino}) adicionada com sucesso.")
    else:
        print(f"Vértice {origem} ou {destino} não encontrado no grafo.")

def adicionar_vertice(G: nx.Graph, vertice: int):
    if vertice not in G.nodes:
        G.add_node(vertice)
    else:
        print(f"Vértice {vertice} já existe no grafo.")

def criar_grafo():
    G = nx.DiGraph()

    num_vertices = int(input("Digite o número de vértices: "))

    for i in range(1, num_vertices + 1):
        adicionar_vertice(G, int(i))

    while True:
        graph.limpar_tela()
        print("Menu:")
        print("1. Adicionar aresta com peso")
        print("2. Mostrar o grafo")
        print("3. Remover vértice")
        print("4. Salvar o grafo em um arquivo .graphml")
        print("5. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            peso = float(input("Peso da aresta: "))

            G.add_edge(origem, destino, weight=peso)
        elif op == '2':
            lib.plotar_grafo(G)
        elif op == '3':
            vertice = input("Vértice a ser removido: ")
            remover_vertice(G, vertice)
        elif op == '4':
            arquivo = input("Nome do arquivo .graphml para salvar(inclua a extensao .graphml): ")
            nx.write_graphml(G, arquivo)
            print(f"Grafo salvo em {arquivo}")
        elif op == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
