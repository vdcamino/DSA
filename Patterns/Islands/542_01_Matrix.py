class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS, COLS = len(mat), len(mat[0])

        visited = set()
        queue = deque()

        # get all border zeroes
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    for row_offset, col_offset in DIRECTIONS:
                        new_row, new_col = row + row_offset, col + col_offset
                        if (
                            new_row in range(ROWS)
                            and new_col in range(COLS)
                            and mat[new_row][new_col] == 1
                        ):
                            queue.append((row, col))

        # bfs starting from border zeroes
        cur_dist = 1
        while queue:
            nodes_in_this_level = len(queue)
            while nodes_in_this_level:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and mat[new_row][new_col] == 1
                        and (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        mat[new_row][new_col] = cur_dist
                nodes_in_this_level -= 1
            cur_dist += 1
        return mat
