from math import degrees

class Graph:
    def __init__(self, node_count: int, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def degree_out(self, u: int) -> int:
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        degree = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                degree += 1
        return degree

    def highest_degree_out(self) -> int:
        max_degree_out = 0
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_out_node_i = self.degree_out(i)
            if max_degree_out < degree_out_node_i:
                max_degree_out = degree_out_node_i
                highest_degree_node = i
        return highest_degree_node

    def highest_degree_in(self) -> int:
        max_degree_in = float("inf")
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_in_node_i = self.degree_in(i)
            if max_degree_in < degree_in_node_i:
                max_degree_in = degree_in_node_i
                highest_degree_node = i
        return highest_degree_node

    def __str__(self):
        repr = ""
        for adj in self.adj_list:
            repr += str(adj) + "\n"
        return repr
    
    def density(self):
        return self.edge_count/(self.node_count * (self.node_count - 1))

    def complete(self):
        #return self.density() == 1
        #return self.edge_count == self.node_count * (self.node_count - 1)
        for u in range(len(self.adj_list)):
            if len(self.adj_list[u]) != self.node_count - 1:
                return False
        return True
                
    def regular(self):
        degree = len(self.adj_list[0])
        for u in range(len(self.adj_list)):
            if len(self.adj_list[u]) != degree:
                return False
        return True

    def complement(self):
        # Returns the complement of a graph
        g2 = Graph(self.node_count)
        for u in range(len(self.adj_list)):
            for i in range(self.node_count):
                if i not in self.adj_list[u] and i != u:
                    g2.add_directed_edge(u, i)
        return g2

    def subgraph(self, g2):
        # Returns true if g2 is a subgraph of self
        if g2.node_count > self.node_count or g2.edge_count > self.edge_count:
            return False
        for u in range(len(self.adj_list)):
            for v in g2.adj_list[u]:
                if v not in self.adj_list[u]:
                    return False
        return True

    def bfs(self, s):
        desc = []
        for v in range(len(self.adj_list)):
            desc.append(0)
        Q = [s]
        R = [s]
        desc[s] = 1
        while len(Q) != 0:
            u = Q.pop(0)
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        return R
    
    def connected(self):
        if len(self.busca_largura(5)) < self.node_count:
            return False
        return True