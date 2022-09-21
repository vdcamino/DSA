from collections import defaultdict


class Graph:
    # constructor
    def __init__(self, V):
        self.V = V
        self.adj_list = defaultdict(list)

    # function to add an edge to the graph
    def addEdge(self, v, w):
        self.adj_list[v].append(w)

    # helper recursive function used by dfs
    def dfs_util(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # recur for all the adjacent nodes of this vertex
        for neighbour in self.adj_list[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    # recursive function that uses the dfs_util helper function
    def dfs(self, starting_node):
        # initialize the visited set
        visited = set()

        # call the recursive helper function to print dfs traversal
        self.dfs_util(starting_node, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 5)
    g.addEdge(1, 4)
    g.addEdge(5, 6)
    g.addEdge(1, 6)
    g.addEdge(3, 3)

    print("Following is a DFS starting from node 1")
    g.dfs(1)
