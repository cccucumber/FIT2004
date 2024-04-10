# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

import sys
import heapq

# Dijkstra's Algorithm using Adjacency Matrix
# Time Complexity: O(V^2)
# Auxiliary Space: O(V)
class DijkstraMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for column in range(self.num_vertices)] for row in range(self.num_vertices)]
    
    def output(self, distance):
        print("Vertex \tDistance from Source")
        for node in range(self.num_vertices):
            print(f"{node}\t{distance[node]}")

    def min_distance(self, distance, visited):
        minimum = sys.maxsize

        for u in range(self.num_vertices):
            if distance[u] < minimum and not visited[u]:
                minimum = distance[u]
                min_index = u

        return min_index
    
    def shortest_path(self, src):
        distance = [sys.maxsize] * self.num_vertices
        distance[src] = 0
        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            x = self.min_distance(distance, visited)
            visited[x] = True

            for y in range(self.num_vertices):
                if self.graph[x][y] > 0 and not visited[y] and distance[y] > distance[x] + self.graph[x][y]:
                    distance[y] = distance[x] + self.graph[x][y]

        self.output(distance)

# Dijkstra's Algorithm using Adjacency List
# Time Complexity: O(E * logV), Where E is the number of edges and V is the number of vertices.
# Auxiliary Space: O(V)
class DijkstraList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = [[] for _ in range(self.num_vertices)]

    def add_edge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def shortest_path(self, src: int):
        priority_queue = []
        heapq.heappush(priority_queue, (0, src))

        distance = [float('inf')] * self.num_vertices
        distance[src] = 0
        
        while priority_queue:
            _, u = heapq.heappop(priority_queue)

            for v, weight in self.adj[u]:
                if distance[v] > distance[u] + weight:
                    distance[v] = distance[u] + weight
                    heapq.heappush(priority_queue, (distance[v], v))

        print("Vertex \tDistance from Source")
        for node in range(self.num_vertices):
            print(f"{node}\t{distance[node]}")

if __name__ == "__main__":
    print("Dijkstra's Algorithm using Adjacency Matrix:")
    g = DijkstraMatrix(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    g.shortest_path(0)

    print("\nDijkstra's Algorithm using Adjacency List:")
    g = DijkstraList(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
 
    g.shortest_path(0)
