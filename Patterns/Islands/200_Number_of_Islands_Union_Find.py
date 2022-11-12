class Solution:
    # global variable to store the number of components
    # accessible and modifiable within union() and find() functions
    count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rank = {}
        parent = {}

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return  # already connected
            if rank[root_v] > rank[root_u]:  # union by rank
                rank[root_v] += rank[root_u]
                parent[root_u] = root_v
            else:
                rank[root_u] += rank[root_v]
                parent[root_v] = root_u
            self.count -= 1

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # path compression
                u = parent[u]
            return u

        for row in range(ROWS):
            for col in range(COLS):
                # create component
                if grid[row][col] == "1":
                    node_id = (row, col)
                    rank[node_id] = 1
                    parent[node_id] = node_id
                    self.count += 1

        for row in range(ROWS):
            for col in range(COLS):
                # merge components with its neighbors
                if grid[row][col] == "1":
                    for row_offset, col_offset in DIRECTIONS:
                        new_row, new_col = row + row_offset, col + col_offset
                        if (
                            new_row in range(ROWS)
                            and new_col in range(COLS)
                            and grid[new_row][new_col] == "1"
                        ):
                            union((row, col), (new_row, new_col))

        return self.count
