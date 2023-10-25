import os
import tkinter as tk
from sys import stderr
from tkinter import filedialog

import lib
import networkx as nx
import matplotlib.pyplot as plt

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
        return
    os.system('clear')

def executar_op(op: int, G: nx.Graph):
    limpar_tela()
    if op == 1:
        # Ordem do grafo
        ordemGrafo = G.number_of_nodes()
        print(f"Ordem do grafo: {ordemGrafo}")
    elif op == 2:
        # Tamanho do grafo
        tamanhoGrafo = G.number_of_edges()
        print(f"Tamanho do grafo: {tamanhoGrafo}")
    elif op == 3:
        # Vizinhos de um vértice
        vertice = input("Digite o vértice: ")
        vizinhos = list(G.neighbors(vertice))
        print(f"Vizinhos do vértice {vertice}: {vizinhos}")
    elif op == 4:
        # Grau de um vértice
        vertice = input("Digite o vértice: ")
        grau = G.degree(vertice)
        print(f"Grau do vértice {vertice}: {grau}")
    elif op == 5:
        # Sequência de graus do grafo
        sequenciaGraus = sorted([grau for _, grau in G.degree()], reverse=True) # type: ignore
        print(f"Sequência de graus do grafo: {sequenciaGraus}")
    elif op == 6:
        # Cálculo da excentricidade de acordo com o vértice.
        v = input("Vértice: ")
        try:
            excentricidade = lib.excentricidade(G, v)
            print(f"Excentricidade do vértice {v}: {excentricidade}")
        except Exception as ex:
            print(f"Excentricidade não está definida. {ex}")
    elif op == 7:
        # Raio do Grafo.
        try:
            raio = lib.raio(G)
            print(f"Raio do grafo: {raio}")
        except Exception as ex:
            print(f"O raio não está definido. {ex}")
    elif op == 8:
        # Diametro do Grafo.
        try:
            diametroGrafo = lib.diametro(G)
            print(f"Diâmetro do grafo: {diametroGrafo}")
        except Exception as ex:
            print(f"O diâmetro não está definido. {ex}")
    elif op == 9:
        # Centro do grafo, mostra a posição do grafo.
        try:
            centroGrafo = lib.centro(G)
            print(f"Centro do grafo: {centroGrafo}")
        except Exception as ex:
            print(f"O centro não está definido. {ex}")
    elif op == 10:
        # Busca em largura (BFS)
        orig = input("Vértice de origem: ")
        arq = input("Nome do arquivo da árvore de largura: ")
        lib.busca_largura(G, orig, arq)
    elif op == 11:
        # Distância e caminho mínimo
        orig = input("Vértice de origem: ")
        dest = input("Vértice de destino: ")
        lib.menor_caminho(G, orig, dest)
    elif op == 12:
        # Centralidade de proximidade
        x = input("Vértice: ")
        try:
            res = lib.centralidade_proximidade(G, x)
            print(f"Centralidade de proximidade de {x}: {res}")
        except Exception as ex:
            print(f"Não foi possível calcular a centralidade de {x}. {ex}")
    elif op == 13:
        # Plotar grafo
        lib.plotar_grafo(G)
    elif op == 14:
        # Plotar árvore de largura
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("GraphML files", "*.graphml")])
        if file_path:
            AL = nx.read_graphml(file_path)
            lib.plotar_grafo(AL)
    # elif op == 15:
    #     # Plotar grafo com pesos e árvore de largura
    #     root = tk.Tk()
    #     root.withdraw()
    #     file_path = filedialog.askopenfilename(filetypes=[("GraphML files", "*.graphml")])
    #     if file_path:
    #         AL = nx.read_graphml(file_path)
    #         nx.draw(AL, with_labels=True, font_weight='bold')
    #         plt.show()
    # elif op == 16:
    #     # Plotar grafo com pesos e caminho mínimo
    #     root = tk.Tk()
    #     root.withdraw()
    #     file_path = filedialog.askopenfilename(filetypes=[("GraphML files", "*.graphml")])
    #     if file_path:
    #         AL = nx.read_graphml(file_path)
    #         nx.draw(AL, with_labels=True, font_weight='bold')
    #         plt.show()
    # elif op == 17:
    #     # Plotar grafo com pesos e centralidade de proximidade
    #     root = tk.Tk()
    #     root.withdraw()
    #     file_path = filedialog.askopenfilename(filetypes=[("GraphML files", "*.graphml")])
    #     if file_path:
    #         AL = nx.read_graphml(file_path)
    #         nx.draw(AL, with_labels=True, font_weight='bold')
    #         plt.show()
    elif op == 18:
        # Voltar
        return
    else:
        # Operações não implementadas
        print(f"Operação não implementada: '{op}'", file=stderr)


def carregar_grafo():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal do tkinter

    file_path = filedialog.askopenfilename(filetypes=[("GraphML files", "*.graphml")])

    if file_path:
        graph = nx.read_graphml(file_path)
        return graph
    else:
        return None
