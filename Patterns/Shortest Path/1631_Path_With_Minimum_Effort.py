class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(k):
            visited = set()
            visited.add((0, 0))

            q = collections.deque()
            q.append((0, 0))

            while q:
                r, c = q.popleft()

                # base case
                if (r, c) == (ROWS - 1, COLS - 1):
                    return True

                for r_offset, c_offset in DIRECTIONS:
                    new_r, new_c = r + r_offset, c + c_offset

                    if (
                        new_r in range(ROWS)
                        and new_c in range(COLS)
                        and (new_r, new_c) not in visited
                    ):
                        cur_diff = abs(heights[new_r][new_c] - heights[r][c])
                        if cur_diff <= k:
                            visited.add((new_r, new_c))
                            q.append((new_r, new_c))

        left = 0
        right = max(heights[r][c] for c in range(COLS) for r in range(ROWS))

        while left < right:
            mid = left + (right - left) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid + 1
        return left


# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         ROWS, COLS = len(heights), len(heights[0])
#         DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         diff_matrix = [[math.inf]*COLS for _ in range(ROWS)]
#         diff_matrix[0][0] = 0
#         visited = set()
#         min_heap = [(0, 0, 0)]  # cur_diff, cur_row, cur_col
#         heapq.heapify(min_heap)
#         while min_heap:
#             cur_diff, cur_row, cur_col = heapq.heappop(min_heap)
#             if (cur_row, cur_col) in visited:
#                 continue
#             if (cur_row, cur_col) == (ROWS - 1, COLS - 1):
#                 return cur_diff
#             visited.add((cur_row, cur_col))
#             for row_offset, col_offset in DIRECTIONS:
#                 new_row = cur_row + row_offset
#                 new_col = cur_col + col_offset
#                 if new_row in range(ROWS) and new_col in range(COLS) and (new_row, new_col) not in visited:
#                     # total cost can never go down in dijkstra (no negative weights)
#                     # that's why we need to have a new dist with at least the calue of cur dist
#                     new_diff = max(cur_diff, abs(heights[new_row][new_col] - heights[cur_row][cur_col]))
#                     # here, the total path cost is the maximum absolute difference, its a different kind of cost function compared to the vanilla adding all costs together along the path
#                     if new_diff < diff_matrix[new_row][new_col]:
#                         diff_matrix[new_row][new_col] = new_diff
#                         heapq.heappush(min_heap, (new_diff, new_row, new_col))

#         # SC = O(m*n)
#         # TC = O(m*n*log(m*n))
