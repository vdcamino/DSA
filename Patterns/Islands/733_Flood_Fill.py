class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(image), len(image[0])

        replaced = image[sr][sc]
        image[sr][sc] = color  # starting point must also be painted
        visited = set()

        queue = collections.deque()
        queue.append((sr, sc))
        while queue:
            cur_row, cur_col = queue.popleft()
            for row_offset, col_offset in DIRECTIONS:
                new_row, new_col = cur_row + row_offset, cur_col + col_offset
                if (
                    new_row in range(ROWS)
                    and new_col in range(COLS)
                    and image[new_row][new_col] == replaced
                    and (new_row, new_col) not in visited
                ):
                    image[new_row][new_col] = color
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        return image
