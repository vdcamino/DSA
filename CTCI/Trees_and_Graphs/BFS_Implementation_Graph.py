from collections import deque

# Graph example
#         4 -- 8
#       /       \
#     6      7   1
#    / \     |   |
#   2   3 -- 5   0


class Graph:
    def __init__(self, V):  # constructor
        self.V = V  # number of vertices
        self.adj_list = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj_list[v].append(w)  # add w to v's list


def BFS(graph, starting_node):
    visited = list()  # list that store the node that we have already visited
    q = deque()  # queue from which we will pop the current node
    visited.append(starting_node)
    q.append(starting_node)
    while q:
        curr = q.popleft()
        for neighbour in graph.adj_list[curr]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.append(neighbour)
    return visited


if __name__ == "__main__":

    myGraph = Graph(9)
    myGraph.addEdge(4, 8)
    myGraph.addEdge(4, 6)
    myGraph.addEdge(6, 3)
    myGraph.addEdge(6, 2)
    myGraph.addEdge(3, 5)
    myGraph.addEdge(5, 7)
    myGraph.addEdge(8, 1)
    myGraph.addEdge(1, 0)

    print(BFS(myGraph, 4))
