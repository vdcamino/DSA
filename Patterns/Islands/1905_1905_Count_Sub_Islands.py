class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid1), len(grid1[0])

        visited = set()

        def bfs(r0, c0):
            queue = collections.deque()
            queue.append((r0, c0))
            # an island will only be counted if all of its nodes are also present in grid1
            valid = 1
            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and (new_row, new_col) not in visited
                        and grid2[new_row][new_col] == 1
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        # check if it invalidates the sub-island constraint
                        if grid1[new_row][new_col] == 0:
                            valid = 0
            return valid

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row, col) not in visited
                    and grid2[row][col] == 1
                    and grid1[row][col] == 1
                ):
                    visited.add((row, col))
                    res += bfs(row, col)

        return res
