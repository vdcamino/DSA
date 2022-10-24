# Python program for Dijkstra's single source shortest path algorithm.
# The program uses adjacency matrix representation for the graph
import math
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [math.inf] * self.V
        dist[src] = 0

        visited = [False] * self.V

        min_heap = [(0, src)]
        heapq.heapify(min_heap)

        while min_heap:
            cur_dist, cur_node = heapq.heappop(min_heap)

            visited[cur_node] = True

            for next_node in range(self.V):
                if (
                    not visited[next_node]
                    and self.graph[cur_node][next_node] > 0
                    and cur_dist + self.graph[cur_node][next_node] < dist[next_node]
                ):
                    dist[next_node] = cur_dist + self.graph[cur_node][next_node]
                    heapq.heappush(min_heap, (dist[next_node], next_node))

        self.printSolution(dist)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]

    g.dijkstra(0)
