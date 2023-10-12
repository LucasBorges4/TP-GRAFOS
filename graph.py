#!/usr/bin/env python3


def main(args):
    from sys import stderr, exit
    import networkx as nx
    import ordemGrafo, tamanhoGrafo, vizinhosVertice, grauVertice, sequenciaGraus, excentricidadeVertice, raioGrafo

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
            ordem = ordemGrafo.ordemGrafo(graph)
            print(f"Ordem do grafo: {ordem}")
        elif op == 2:
            tam = tamanhoGrafo.tamanhoGrafo(graph)
            print(f"Tamanho do grafo: {tam}")
        elif op == 3:
            vertice = input("Digite o vértice: ")
            vizinhos = vizinhosVertice.vizinhosVertice(graph, vertice)
            print(f"Vizinhos do vértice {vertice}: {vizinhos}")
        elif op == 4:
            vertice = input("Digite o vértice: ")
            grau = grauVertice.grauVertice(graph, vertice)
            print(f"Grau do vértice {vertice}: {grau}")
        elif op == 5:
            sequenciaGraus = sequenciaGraus.sequenciaGraus(graph)
            print(f"Sequência de graus do grafo: {sequenciaGraus}")
        elif op == 6:
            vertice = input("Digite o vértice: ")
            excentricidade = excentricidadeVertice.excentricidadeVertice(graph, vertice)
            print(f"Excentricidade do vértice {vertice}: {excentricidade}")
        elif op == 7:
            raioGrafo = raioGrafo.raioGrafo(graph)
            print(f"Raio do grafo: {raioGrafo}")
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
