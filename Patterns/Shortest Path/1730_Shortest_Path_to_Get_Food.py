class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque()
        visited = set()

        # get all the starting points
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "#":
                    queue.append((row, col))
                    visited.add((row, col))

        # check if there is food
        if not queue:
            return -1

        res = 1
        while queue:
            nodes_in_this_level = len(queue)
            while nodes_in_this_level:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        if grid[new_row][new_col] == "*":
                            return res
                        elif grid[new_row][new_col] == "O":
                            queue.append((new_row, new_col))
                nodes_in_this_level -= 1
            res += 1
        return -1
