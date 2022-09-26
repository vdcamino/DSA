class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            # base case
            if (
                r not in range(m)
                or c not in range(n)
                or (r, c) in visited
                or heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r0, c0 = r + dr, c + dc
                dfs(r0, c0, visited, heights[r][c])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])

        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])

        res = list()
        for r in range(m):
            for c in range(n):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res
