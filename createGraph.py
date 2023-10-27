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

import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo():
    G = nx.DiGraph()

    num_vertices = int(input("Digite o número de vértices: "))

    for i in range(1, num_vertices + 1):
        G.add_node(str(i))  # Adiciona vértices com rótulos de 1 a num_vertices

    while True:
        print("\nMenu:")
        print("1. Adicionar aresta com peso")
        print("2. Adicionar aresta sem peso")
        print("3. Mostrar o grafo")
        print("4. Remover vértice")
        print("5. Salvar o grafo em um arquivo .graphml")
        print("6. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")

            # Verifique se os vértices existem antes de adicionar a aresta
            if G.has_node(origem) and G.has_node(destino):
                peso = float(input("Peso da aresta: "))
                G.add_edge(origem, destino, weight=peso)
                print("Aresta com peso adicionada.")
            else:
                print("Pelo menos um dos vértices especificados não existe no grafo.")
        elif op == '2':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")

            # Verifique se os vértices existem antes de adicionar a aresta
            if G.has_node(origem) and G.has_node(destino):
                G.add_edge(origem, destino)
                print("Aresta sem peso adicionada.")
            else:
                print("Pelo menos um dos vértices especificados não existe no grafo.")
        elif op == '3':
            lib.plotar_grafo(G)  # Chama a função para plotar o grafo
        elif op == '4':
            vertice = input("Vértice a ser removido: ")
            G.remove_node(vertice)
        elif op == '5':
            arquivo = input("Nome do arquivo .graphml para salvar (inclua a extensão .graphml): ")
            nx.write_graphml(G, arquivo)
            print(f"Grafo salvo em {arquivo}")
        elif op == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

