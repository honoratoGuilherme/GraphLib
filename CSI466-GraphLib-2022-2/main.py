from graph import Graph

# g1 = Graph(4, adj_list = [])
# g1.add_directed_edge(0, 1)
# g1.add_directed_edge(0, 2)
# g1.add_directed_edge(0, 3)
# g1.add_directed_edge(1, 0)
# g1.add_directed_edge(1, 2)
# g1.add_directed_edge(1, 3)
# g1.add_directed_edge(2, 0)
# g1.add_directed_edge(2, 1)
# g1.add_directed_edge(2, 3)
# g1.add_directed_edge(3, 0)
# g1.add_directed_edge(3, 1)
# g1.add_directed_edge(3, 2)

# print("GRAPH 1:", g1.adj_list)
# print("DEGREE_OUT(0):", g1.degree_out(0))
# print("DEGREE_OUT(1):", g1.degree_out(1))
# print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
# print("DEGREE_IN(0):", g1.degree_in(0))
# print("DEGREE_IN(1):", g1.degree_in(1))

# print(g1.density())
# print(g1.complete())
# print(g1.regular())
# print(g1.complement())

g1 = Graph(3, adj_list=[])
g1.add_undirected_edge(0, 1)
g1.add_undirected_edge(0, 2)

g2 = Graph(3, adj_list=[])
g2.add_undirected_edge(1, 2)
print("G2 IS SUBGRAPH OF G1?", g1.subgraph(g2))