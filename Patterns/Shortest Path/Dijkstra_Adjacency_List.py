import heapq


class Graph:
    def __init__(self, V):
        self.adj_list = {i: [] for i in range(V)}
        self.V = V

    def addEdge(self, u, v, w):
        self.adj_list[u].append((v, w))

    def findShortestPath(self, start, end):
        minHeap = []
        heapq.heapify(minHeap)
        # best distance we have found so far for node v
        dist = [float("+inf")] * self.V
        dist[start] = 0
        # the first time you visit a node, you are sure to have found the best path for this node (thanks to the minHeap)
        visited = [False] * self.V
        # previous node in the best path we have found so far for v
        prev = [-1] * self.V

        heapq.heappush(minHeap, (0, start))

        while minHeap:
            # greedy: we always pop from the minHeap the node that is closest to the source
            curDist, curNode = heapq.heappop(minHeap)
            # even though the first time the node is popped from the heap we get its shortest distance, a node can be pushed to the heap more than once
            if visited[curNode]:
                continue
            visited[curNode] = True
            # the first time we pop the destination node, we are already sure that this is its best path
            if curNode == end:
                break
            for neighborNode, neighborCost in self.adj_list[curNode]:
                if curDist + neighborCost < dist[neighborNode]:
                    dist[neighborNode] = curDist + neighborCost
                    prev[neighborNode] = curNode
                    heapq.heappush(minHeap, (curDist + neighborCost, neighborNode))

        shortestPath = []
        curNode = end
        while curNode != start:
            shortestPath.insert(0, curNode)
            curNode = prev[curNode]
        shortestPath.insert(0, start)

        print("Shortest Path from " + str(start) + " to " + str(end) + ":")
        print(*shortestPath, sep=" -> ")
        print("The total cost is: ")
        print(dist[end])


if __name__ == "__main__":
    mygraph = Graph(3)
    mygraph.addEdge(0, 1, 100)
    mygraph.addEdge(1, 2, 100)
    mygraph.addEdge(0, 2, 500)

    mygraph.findShortestPath(0, 2)
