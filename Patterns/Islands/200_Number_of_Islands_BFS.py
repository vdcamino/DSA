class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [0, -1], [0, 1], [-1, 0]]

        res = 0
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))

            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and grid[new_row][new_col] == "1"
                        and not visited[new_row][new_col]
                    ):
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and not visited[row][col]:
                    visited[row][col] = True
                    res += 1
                    bfs(row, col)

        return res


# TC = O(N), where N = number of cells
# SC:
# - If we can modify the data:
# O(min(ROWS, COLS)), the size of the queue is proportional to the smallest dimension because that's what limits the queue size
# Example: Grid of dimensions 3x1000
# ......QXXXQ.........
# ....QXXXXXQ........
# ......QXXXQ.........
# --> The row dimension (3) is the one that dictates the space complexity
# - If we cannot modify the data, O(ROWS*COLS) because of the visited set/array
