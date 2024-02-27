from queue import Queue
from math import inf 

NIL = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

'''
def amount_odd(C):
    n = 0
    for i in C:
        if (i % 2 != 0):
            n += 1
    return n

def amount_even(C):
    m = 0
    for i in C:
        if (i % 2 == 0):
            m += 1
    return m
''' 

class bipartite_graph(object):
    def __init__(self, C, m, n):
        self.C = C
        self.right_nodes = m
        self.left_nodes = n
        self.adjacents_left = [[] for _ in range(m + 1)]

    def add_edges(self):
        for i in range(len(self.C)):
            for j in range(i + 1, len(self.C)):
                    if is_prime((self.C[i] + self.C[j])):
                        if (self.C[i] % 2 != 0):
                            self.adjacents_left[i + 1].append(j + 1)
                        else:
                            self.adjacents_left[j + 1].append(i + 1)
 
    def bfs(self):
        Q = Queue()
        for u in range(1, self.right_nodes + 1):
            if self.u_pairs[u] == NIL:
                self.left_side_vertices_distance[u] = 0
                Q.put(u)
            else:
                self.left_side_vertices_distance[u] = inf
        self.left_side_vertices_distance[NIL] = inf

        while not Q.empty():
            u = Q.get()
            if self.left_side_vertices_distance[u] < self.left_side_vertices_distance[NIL]:
                for v in self.adjacents_left[u]:
                    if self.left_side_vertices_distance[self.v_pairs[v]] == inf:
                        self.left_side_vertices_distance[self.v_pairs[v]] = self.left_side_vertices_distance[u] + 1
                        Q.put(self.v_pairs[v])
        return self.left_side_vertices_distance[NIL] != inf
 
    def dfs(self, u):
        if u != NIL:
            for v in self.adjacents_left[u]:
                if self.left_side_vertices_distance[self.v_pairs[v]] == self.left_side_vertices_distance[u] + 1:
                    if self.dfs(self.v_pairs[v]):
                        self.v_pairs[v] = u
                        self.u_pairs[u] = v
                        return True
            self.left_side_vertices_distance[u] = inf
            return False
        return True
 
    def hopcroft_karp(self):
        # Para cada vértice u en el lado izquierdo,
        # se guarda el vértice v en el lado derecho
        # que está emparejado con u en el matching.
        self.u_pairs = [0 for _ in range(self.right_nodes+1)]
 
        # Igual que con u pero, en este caso, para los
        # vértices v.
        self.v_pairs = [0 for _ in range(self.left_nodes+1)]
 
        # distancias de los vértices del lado izquierdo (u)
        # desde la fuente en el augmenting path.
        self.left_side_vertices_distance = [0 for _ in range(self.right_nodes+1)]

        result = 0
 
        while self.bfs():
            for u in range(1, self.right_nodes + 1):
                if self.u_pairs[u] == NIL and self.dfs(u):
                    result += 1
        return result
 
 
C = [1, 2, 3, 4, 5, 11]
g = bipartite_graph(C, len(C), len(C))
g.add_edges()
print("El número mínimo de vértices para eliminar es %d" % g.hopcroft_karp())