#!/usr/bin/env python3
import graph, lib, createGraph

OPS = {
    1 : "Ordem do grafo"               ,
    2 : "Tamanho do grafo"             ,
    3 : "Vizinhos de um vértice"       ,
    4 : "Grau de um vértice"           ,
    5 : "Sequência de graus do grafo"  ,
    6 : "Excentricidade de um vértice" ,
    7 : "Raio do grafo"                ,
    8 : "Diâmetro do grafo"            ,
    9 : "Centro do grafo"              ,
    10: "Busca em largura (BFS)"       ,
    11: "Distância e caminho mínimo"   ,
    12: "Centralidade de proximidade"  ,
    13: "Plotar grafo"                 ,
    14: "Plotar árvore de largura"     ,
    15: "Plotar grafo com pesos"       ,
    # 16: "Plotar grafo com pesos e árvore de largura",
    # 17: "Plotar grafo com pesos e caminho mínimo",
    # 18: "Plotar grafo com pesos e centralidade de proximidade",
    19: "Voltar",
}

def main():
    grafo = None

    while True:
        graph.limpar_tela()
        print("===== MENU =====")

        print("1. Carregar grafo")
        print("2. Criar grafo")
        if grafo:
            print("3. Informações do grafo")
        print ("0. Sair")

        op = input("Digite o número da opção escolhida: ")

        if op == '0':
            print("Ok! Saindo...")
            break
        elif op == '1':
            grafo = graph.carregar_grafo()
            if grafo:
                print(f"Grafo {grafo} lido com sucesso!")
            else:
                print("Nenhum grafo foi carregado")
                continue
        elif op == '2':
            grafo = createGraph.criar_grafo()
            if grafo:
                print(f"Grafo {grafo} criado com sucesso!")
            else:
                print("Nenhum grafo foi criado")
                continue
        elif op == '3':
            if grafo:
                graph.limpar_tela()
                print("==== OPERAÇÕES ====")
                for n, desc in OPS.items():
                    print(f"{n}. {desc}")
                op = int(input("Digite o número da opção escolhida: "))

                if op not in OPS:
                    print("Opção não reconhecida, tente novamente")
                    continue
                graph.executar_op(op, grafo)
            else:
                print("Nenhum grafo foi carregado")
                continue
        else:
            print("Opção não reconhecida, tente novamente")
            continue

        resp = input("\nDeseja executar mais uma operação? (S/n) ")
        if resp != "S" and resp != "s":
            print("Ok! Saindo...")
            break

    print("Fim da execução!")

if __name__ == "__main__":
    main()