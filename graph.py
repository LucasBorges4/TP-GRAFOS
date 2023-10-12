#!/usr/bin/env python3


def main(args):
    from sys import stderr, exit
    import networkx as nx
    import matplotlib.pyplot as plt

    try:
        # Leitura do grafo em GraphML
        graph = nx.read_graphml(args[0])
        print(f"Grafo {args[0]} lido com sucesso!")
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
    except nx.NetworkXError:
        # Ocorreu algum erro (i.e. o arquivo não é válido)
        print(f"Não foi possível ler o grafo {args[0]}...", file=stderr)
        exit(1)

    prossiga = True

    while prossiga:
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
            ordemGrafo = graph.number_of_nodes()
            print(f"Ordem do grafo: {ordemGrafo}")
        elif op == 2:
            tamanhoGrafo = graph.number_of_edges()
            print(f"Tamanho do grafo: {tamanhoGrafo}")
        elif op == 3:
            vertice = input("Digite o vértice: ")
            vizinhos = list(graph.neighbors(vertice))
            print(f"Vizinhos do vértice {vertice}: {vizinhos}")
        elif op == 4:
            vertice = input("Digite o vértice: ")
            grau = graph.degree(vertice)
            print(f"Grau do vértice {vertice}: {grau}")
        elif op == 5:
            sequenciaGraus = sorted([grau for vertice, grau in graph.degree()], reverse=True)
            print(f"Sequência de graus do grafo: {sequenciaGraus}")
        elif op == 6:
            vertice = input("Digite o vértice: ")
            excentricidade = nx.eccentricity(graph, v=vertice)
            print(f"Excentricidade do vértice {vertice}: {excentricidade}")
        elif op == 7:
            raio = nx.radius(graph)
            print(f"Raio do grafo: {raio}")
        elif op == 8:
            diametroGrafo = nx.diameter(graph)
            print(f"Diâmetro do grafo: {diametroGrafo}")
        elif op == 9:
            centroGrafo = nx.center(graph)
            print(f"Centro do grafo: {centroGrafo}")
        elif op == 14:
            print("Saindo...")
            break
        else:
            # Por enquanto, todas as operações não implementadas caem aqui
            print(f"Operação {op} ainda sem implementação...", file=stderr)
        print()


        prossiga = input("Deseja realizar outra operação? (s/n) ") == "s"
        print("\n")

    print("Fim da execução!")
if __name__ == "__main__":
    from sys import argv
    main(argv[1:])
