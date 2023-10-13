#!/usr/bin/env python3

import networkx as nx
from sys import stderr, exit
from lib import shortest_path

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
        print("== OPERAÇÕES ==")
        print("1. Obter a ordem do grafo")
        print("2. Obter o tamanho do grafo")
        print("3. Determinar os vizinhos de um vértice")
        print("4. Determinar o grau de um vértice")
        print("5. Obter a sequência de graus do grafo")
        print("6. Determinar a excentricidade de um vértice")
        print("7. Determinar o raio do grafo")
        print("8. Determinar o diâmetro do grafo")
        print("9. Determinar o centro do grafo")
        print("10. Determinar o centro do grafo")
        print("11. Realizar busca em largura (BFS)")
        print("12. Obter a distância e caminho mínimo entre dois vértices")
        print("13. Calcular a centralidade de proximidade de um vértice")
        print("14. Sair")

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
        elif op == 12:
            # Caminho mínimo entre dois vértices
            src = input("Vértice de origem: ")
            dst = input("Vértice de destino: ")
            shortest_path(graph, src, dst)
        elif op == 14:
            print("Saindo...")
            break
        else:
            # Por enquanto, todas as operações não implementadas caem aqui
            print(f"Operação {op} ainda sem implementação...", file=stderr)
        print()


if __name__ == "__main__":
    from sys import argv
    main(argv[1:])
