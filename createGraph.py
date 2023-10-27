import lib
import networkx as nx

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

def criar_grafo():
    G = nx.DiGraph()

    num_vertices = int(input("Digite o número de vértices: "))

    for i in range(1, num_vertices + 1):
        G.add_node(str(i))  # Adiciona vértices com rótulos de 1 a num_vertices

    while True:
        print("\nMenu:")
        print("1. Adicionar aresta com peso")
        print("2. Adicionar aresta sem peso")
        print("3. Adicionar aresta não direcionada com peso")
        print("4. Adicionar aresta não direcionada sem peso")
        print("5. Remover aresta")
        print("6. Remover vértice")
        print("7. Mostrar o grafo")
        print("8. Salvar o grafo em um arquivo .graphml")
        print("9. Sair")

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
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")

            # Verifique se os vértices existem antes de adicionar a aresta
            if G.has_node(origem) and G.has_node(destino):
                peso = float(input("Peso da aresta: "))
                G.add_edge(origem, destino, weight=peso)
                G.add_edge(destino, origem, weight=peso)  # Adicione a aresta no sentido oposto
                print("Aresta não direcionada com peso adicionada.")
            else:
                print("Pelo menos um dos vértices especificados não existe no grafo.")
        elif op == '4':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")

            # Verifique se os vértices existem antes de adicionar a aresta
            if G.has_node(origem) and G.has_node(destino):
                G.add_edge(origem, destino)
                G.add_edge(destino, origem)  # Adicione a aresta no sentido oposto
                print("Aresta não direcionada sem peso adicionada.")
            else:
                print("Pelo menos um dos vértices especificados não existe no grafo.")
        elif op == '5':
            origem = input("Vértice de origem da aresta a ser removida: ")
            destino = input("Vértice de destino da aresta a ser removida: ")

            # Verifique se a aresta existe antes de removê-la
            if G.has_edge(origem, destino):
                G.remove_edge(origem, destino)
                print("Aresta removida.")
            else:
                print("Aresta não encontrada no grafo.")
        elif op == '6':
            vertice = input("Vértice a ser removido: ")
            G.remove_node(vertice)
        elif op == '7':
            lib.plotar_grafo(G)  # Chama a função para plotar o grafo
        elif op == '8':
            arquivo = input("Nome do arquivo .graphml para salvar (inclua a extensão .graphml): ")
            nx.write_graphml(G, arquivo)
            print(f"Grafo salvo em {arquivo}")
        elif op == '9':
            break
        else:
            print("Opção inválida. Tente novamente.")
