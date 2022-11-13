class Solution:
    nb_components = 0

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        rank = {}
        for i in range(n):
            parent[i] = i
            rank[i] = 1
            self.nb_components += 1

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
                rank[root_u] += rank[root_v]
                del rank[root_v]
            else:
                parent[root_u] = root_v
                rank[root_v] += rank[root_u]
                del rank[root_u]
            self.nb_components -= 1

        for u, v in edges:
            union(u, v)

        if len(rank) == 1:
            return 0

        # If we calculate the result by getting all the combinations of 2 with itertools.combinations(rank.values(), 2)
        # and then multiplying + adding all the combinations, it woud give us TLF

        # The tricky to get the sum of products in a more efficient way is to use prefix sum
        # Example: [4, 2, 1]
        # (4*2) + (4*1) + (2*1) can be rewritten as: (4*2) + (4 + 2)*1
        # If we generalize this approach for [a, b, c, d, e]
        # --> (a*b) + (a + b)*c + (a + b + c)*d + (a + b + c + d)*e

        group_count = list(rank.values())
        res = 0
        prefix_sum = group_count[0]
        for i in range(1, len(group_count)):
            res += prefix_sum * group_count[i]
            prefix_sum += group_count[i]
        return res
