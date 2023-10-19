#!/usr/bin/env python3

import lib
import networkx as nx
from sys import stderr, exit

OPS = {
    1 : "Ordem do grafo"               ,
    2 : "Tamanho do grafo"             ,
    3 : "Vizinhos de um vértice"       ,
    4 : "Grau de um vértice"           ,
    5 : "Sequência de graus do grafo"  ,
    6 : "Excentricidade de um vértice" ,
    7 : "Raio do grafo"                ,
    9 : "Diâmetro do grafo"            ,
    10: "Centro do grafo"              ,
    11: "Busca em largura (BFS)"       ,
    12: "Distância e caminho mínimo"   ,
    13: "Centralidade de proximidade"  ,
}

def executar_op(op: int, G: nx.Graph):
    if op == 1:
        # Ordem do grafo
        ordem = G.number_of_nodes()
        print(f"Ordem do grafo: {ordem}")
    elif op == 2:
        # Tamanho do grafo
        tam = G.number_of_edges()
        print(f"Tamanho do grafo: {tam}")
    elif op == 6:
        # Cálculo da excentricidade de acordo com o vértice.
        v = input("Vértice: ")
        excentricidade = lib.excentricidade(G, v)
        print(f"Excentricidade do vértice {v}: {excentricidade}")
    elif op == 7:
        # Raio do Grafo.
        raio = lib.raio(G)
        print(f"Raio do grafo: {raio}")
    elif op == 8:
        # Diametro do Grafo.
        diametro = lib.diametro(G)
        print(f"Diametro do grafo: {diametro}")
    elif op == 9:
        # Centro do grafo, mostra a posição do grafo.
        centro = lib.centro(G)
        print(f"Posição do centro do grafo: {centro}")
    elif op == 11:
        # Busca em largura (BFS)
        orig = input("Vértice de origem: ")
        arq = input("Nome do arquivo da árvore de largura: ")
        lib.busca_largura(G, orig, arq)
    elif op == 12:
        # Distância e caminho mínimo
        orig = input("Vértice de origem: ")
        dest = input("Vértice de destino: ")
        lib.menor_caminho(G, orig, dest)
    elif op == 13:
        # Centralidade de proximidade
        x = input("Vértice: ")
        res = lib.centralidade_proximidade(G, x)
        print(f"Centralidade de proximidade de {x}: {res}")
    else:
        # Operações não implementadas
        print(f"Operação não implementada: '{OPS[op]}'", file=stderr)

def main(args):
    try:
        # Leitura do grafo em GraphML
        G = nx.read_graphml(args[0])
        print(f"Grafo {args[0]} lido com sucesso!")
    except nx.NetworkXError:
        # Ocorreu algum erro (i.e. o arquivo não é válido)
        print(f"Não foi possível ler o grafo {args[0]}...", file=stderr)
        exit(1)

    while True:
        # Exibição das operações
        print("== OPERAÇÕES ==")
        for n, desc in OPS.items():
            print(f"{n}. {desc}")

        # Leitura da operação desejada
        op = int(input("Digite o número da opção escolhida: "))
        if op not in OPS:
            print("Opção não reconhecida, tente novamente")
            continue

        # Execução da operação
        executar_op(op, G)
        resp = input("\nDeseja executar mais uma operação? (S/n) ")
        if resp != "S" and resp != "s":
            print("Ok! Saindo...")
            break

if __name__ == "__main__":
    from sys import argv
    main(argv[1:])
