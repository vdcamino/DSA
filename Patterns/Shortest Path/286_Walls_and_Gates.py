class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited = set()
        queue = collections.deque()

        # traverse matrix and append gates coordinates to the queue
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col))

        # bfs starting from all the gates
        count = 1
        while queue:
            # bfs all the nodes in the current level at the same time
            for _ in range(len(queue)):
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and (new_row, new_col) not in visited
                        and rooms[new_row][new_col] != -1
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        rooms[new_row][new_col] = count
            count += 1
