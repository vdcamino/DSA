class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Approach:
        # Save the relative position of all the nodes to the current top left node
        # e.g, isand_type = (0, 1, 1, 1, 1, 0)
        # Use this key to store all the island types that have been discovered during the traversal
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        island_types = set()
        visited = set()

        def bfs(r0, c0):
            nonlocal cur_top_left
            island_type = []
            queue = collections.deque()
            queue.append((r0, c0))
            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] == 1
                    ):
                        visited.add((new_row, new_col))
                        island_type.append(new_row - cur_top_left[0])
                        island_type.append(new_col - cur_top_left[1])
                        queue.append((new_row, new_col))
            island_types.add(tuple(island_type))

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    visited.add((row, col))
                    cur_top_left = (row, col)
                    bfs(row, col)
        return len(island_types)
