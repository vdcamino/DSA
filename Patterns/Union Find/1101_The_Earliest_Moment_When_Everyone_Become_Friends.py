class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # if there are less than n - 1 edges, impossible to have all elements connected
        if len(logs) < n - 1:
            return -1

        # sort the input by timestamp
        logs.sort(key=lambda x: x[0])

        # create components
        rank = {i: 1 for i in range(n)}
        parent = {i: i for i in range(n)}
        self.nb_components = n

        # union-find functions
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            root_u, root_v = find(u), find(v)
            # case already connected
            if root_u == root_v:
                return
            # merge keeping the highest rank as root
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
                rank[root_u] += rank[root_v]
            else:
                parent[root_u] = root_v
                rank[root_v] += rank[root_u]
            self.nb_components -= 1

        # read input and perform merges
        for timestamp, friend_1, friend_2 in logs:
            union(friend_1, friend_2)
            if self.nb_components == 1:
                return timestamp
        return -1
