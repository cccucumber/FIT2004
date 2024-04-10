# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

import sys
import heapq

# Prim's Minimum Spanning Tree (MST) Algorithm using Adjacency Matrix
# Time Complexity: O(V^2)
# Auxiliary Space: O(V)
class PrimMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for column in range(num_vertices)] for row in range(num_vertices)]

    def output(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.num_vertices):
            print(f"{parent[i]}-{i}\t{self.graph[i][parent[i]]}")
    
    def min_distance(self, distance, visited):
        minimum = sys.maxsize

        for u in range(self.num_vertices):
            if distance[u] < minimum and not visited[u]:
                minimum = distance[u]
                min_index = u

        return min_index
    
    def min_spanning_tree(self):
        distance = [sys.maxsize] * self.num_vertices
        distance[0] = 0
        parent = [None] * self.num_vertices
        parent[0] = -1
        visited = [False] * self.num_vertices
        
        for _ in range(self.num_vertices):
            x = self.min_distance(distance, visited)
            visited[x] = True

            for y in range(self.num_vertices):
                if self.graph[x][y] > 0 and not visited[y] and distance[y] > self.graph[x][y]:
                    distance[y] = self.graph[x][y]
                    parent[y] = x
        
        self.output(parent)


# Prim's Minimum Spanning Tree (MST) Algorithm using Adjacency List
# Time Complexity: O(E*log(E)) where E is the number of edges
# Auxiliary Space: O(V^2) where V is the number of vertex
def prim_list(num_vertices, num_edges, edges):
    adj = [[] for _ in range(num_vertices)]
    for i in range(num_edges):
        u, v, weight = edges[i]
        adj[u].append((v, weight))
        adj[v].append((u, weight))
    
    priority_queue = []
    visited = [False] * num_vertices
    result = 0

    heapq.heappush(priority_queue, (0, 0))

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)
        if visited[u]:
            continue
        result += weight
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(priority_queue, (weight, v))

    return result

if __name__ == '__main__':
    print("Prim's Minimum Spanning Tree (MST) Algorithm using Adjacency Matrix")
    g = PrimMatrix(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
 
    g.min_spanning_tree()

    print("\nPrim's Minimum Spanning Tree (MST) Algorithm using Adjacency List")
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    
    print(prim_list(3, 3, graph))
