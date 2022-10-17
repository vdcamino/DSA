class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        # K + 1 iterations of Bellman Ford
        for i in range(K + 1):
            dist_aux = dist.copy()
            # Iterate over all the edges
            for s, e, w in flights:
                curDist = dist[s]
                # Relax the edge if possible
                if curDist + w < dist_aux[e]:
                    dist_aux[e] = curDist + w
            dist = dist_aux[:]
        return -1 if dist[dst] == float("inf") else dist[dst]
