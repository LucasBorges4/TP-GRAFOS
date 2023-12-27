import networkx as nx

G1 = nx.DiGraph()
G1.add_weighted_edges_from([(1, 2, 3), (2, 3, 5), (3, 1, 4)])

G2 = nx.Graph()
G2.add_weighted_edges_from([(1, 2, 3), (2, 3, 5), (3, 1, 4)])

G3 = nx.DiGraph()
G3.add_weighted_edges_from([(1, 2, 3), (2, 3, 5), (3, 1, 4), (3, 2, 2)])

G4 = nx.Graph()
G4.add_weighted_edges_from([(1, 2, 3), (2, 3, 5), (3, 1, 4), (3, 2, 2)])

G5 = nx.Graph()
G5.add_edges_from([(1, 2), (2, 3), (3, 1)])

G6 = nx.DiGraph()
G6.add_weighted_edges_from([(1, 2, 3), (1, 3, 4), (2, 4, 1), (3, 4, 2), (4, 5, 5)])

nx.write_graphml(G1, "grafo1.graphml")
nx.write_graphml(G2, "grafo2.graphml")
nx.write_graphml(G3, "grafo3.graphml")
nx.write_graphml(G4, "grafo4.graphml")
nx.write_graphml(G5, "grafo5.graphml")
nx.write_graphml(G6, "grafo6.graphml")
