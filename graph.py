#!/usr/bin/env python3

import networkx as nx
from sys import argv, stderr, exit

from lucas import excentricidade_Do_Vertice, raio_Do_Grafo, diametro_Do_Grafo, centro_Do_Grafo

def main(args):

    try:
        # Leitura do grafo em GraphML
        graph = nx.read_graphml(args[0])
        print(f"Grafo {args[0]} lido com sucesso!")
    except nx.NetworkXError:
        # Ocorreu algum erro (i.e. o arquivo não é válido)
        print(f"Não foi possível ler o grafo {args[0]}...", file=stderr)
        exit(1)

    while True:
        # Menu bem simples
        print("== OPERAÇÕES ==\n"
            "1. Obter a ordem do grafo\n"
            "2. Obter o tamanho do grafo\n"
            "3. Determinar os vizinhos de um vértice\n"
            "4. Determinar o grau de um vértice\n"
            "5. Obter a sequência de graus do grafo\n"
            "6. Determinar a excentricidade de um vértice\n"
            "7. Determinar o raio do grafo\n"
            "8. Determinar o diâmetro do grafo\n"
            "9. Determinar o centro do grafo\n"
            "10. Determinar o centro do grafo\n"
            "11. Realizar busca em largura (BFS)\n"
            "12. Obter a distância e caminho mínimo entre dois vértices\n"
            "13. Calcular a centralidade de proximidade de um vértice\n"
            "14. Sair")

        # Leitura da operação desejada
        op = int(input("Digite o número da opção escolhida: "))
        if op < 0 and op > 14:
            print("Opção não reconhecida, tente novamente")
            continue

        # Realização da operação desejada
        if op == 1:
            ordem = graph.number_of_nodes()
            print(f"Ordem do grafo: {ordem}")
        
        elif op == 2:
            tam = graph.number_of_edges()
            print(f"Tamanho do grafo: {tam}")
            
        elif op == 6:
            # Cálculo da excentricidade de acordo com o vértice.
            vertices = list(graph.nodes())
            TAM = vertices.__len__()
            print(TAM)
            nodo_escolhido = int(input("Qual nodo você deseja escolher para calcular a excentricidade?"))
            excentricidade = excentricidade_Do_Vertice(graph, vertices[nodo_escolhido - 1])
            print(f"Excentricidade do grafo: {excentricidade}")
        
        elif op == 7:
            # Raio do Grafo.
            raio = raio_Do_Grafo(graph)
            print(f"Raio do grafo: {raio}")
        
        elif op == 8:
            # Diametro do Grafo.
            diametro = diametro_Do_Grafo(graph)
            print(f"Diametro do grafo: {diametro}")
        
        elif op == 9:
            # Centro do grafo, mostra a posição do grafo.
            centro = centro_Do_Grafo(graph)
            centro = int(centro[0]) + 1
            print(f"Posição do centro do grafo: {centro}")
        
        elif op == 14:
            print("Saindo...")
            break
        
        else:
            # Por enquanto, todas as operações não implementadas caem aqui
            print(f"Operação {op} ainda sem implementação...", file=stderr)
        
        print()


if __name__ == "__main__":
    main(argv[1:])
