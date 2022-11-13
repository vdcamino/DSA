class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0)]  # just go right and down
        ROWS, COLS = len(land), len(land[0])

        res = []
        visited = set()

        def bfs(r0, c0):
            queue = collections.deque()
            queue.append((r0, c0))
            cur_farm = [r0, c0]
            while queue:
                cur_row, cur_col = queue.popleft()
                right_bottom = [cur_row, cur_col]
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and land[new_row][new_col] == 1
                        and (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            res.append(cur_farm + right_bottom)

        for row in range(ROWS):
            for col in range(COLS):
                if land[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    bfs(row, col)

        return res
