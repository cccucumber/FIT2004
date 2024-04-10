# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

# Kruskal’s Minimum Spanning Tree (MST) Algorithm using the Union-Find Algorithm to detect Cycles
# Time Complexity: O(E * logE) or O(E * logV) - Sorting of edges takes O(E * logE) time, and the value of E can be at most O(V^2), so O(logV) == O(logE)
# Auxiliary Space: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
class Kruskal:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []
    
    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def _find(self, parent, i): # O(logV)
        if parent[i] != i:
            parent[i] = self._find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y): # O(logV)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    
    def min_spanning_tree(self):
        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent, rank = [], []

        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        while e < self.num_vertices - 1:
            # pick the smallest edge
            u, v, weight = self.graph[i]
            i = i + 1
            x = self._find(parent, u)
            y = self._find(parent, v)

            # include edge if it doesnt cause cycle
            if x != y:
                e = e + 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)
        
        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimum_cost)

if __name__ == '__main__': 
    g = Kruskal(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.min_spanning_tree()
