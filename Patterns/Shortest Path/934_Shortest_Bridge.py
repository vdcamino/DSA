class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        # helper function to determine if a coordinate is valid
        def isValidCoord(row, col):
            return row in range(ROWS) and col in range(COLS)

        visited = set()

        # dfs to find the first island and mark it as visited
        def dfs(row, col):
            if (
                not isValidCoord(row, col)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return
            visited.add((row, col))
            for row_offset, col_offset in DIRECTIONS:
                new_row, new_col = row + row_offset, col + col_offset
                dfs(new_row, new_col)

        # bfs to find the shortest path between the first island and the second island
        def bfs():
            res = 0
            queue = collections.deque()
            queue.extend(visited)
            while queue:
                nodes_in_this_level = len(queue)
                while nodes_in_this_level:
                    cur_row, cur_col = queue.popleft()
                    for row_offset, col_offset in DIRECTIONS:
                        new_row, new_col = cur_row + row_offset, cur_col + col_offset
                        if (
                            isValidCoord(new_row, new_col)
                            and (new_row, new_col) not in visited
                        ):
                            visited.add((new_row, new_col))
                            if grid[new_row][new_col] == 0:
                                queue.append((new_row, new_col))
                            else:
                                return res
                    nodes_in_this_level -= 1
                res += 1

        # find first island, perform dfs to mark it and then perform bfs from it to find the second
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return bfs()
