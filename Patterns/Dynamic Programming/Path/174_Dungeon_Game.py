class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dp = [[+inf for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        dp[ROWS][COLS - 1] = 1

        def minNextCellHealth(row, col):
            return min(dp[row][col + 1], dp[row + 1][col])

        def minCurCellHealth(row, col):
            x = minNextCellHealth(row, col) - dungeon[row][col]
            return max(1, x)

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                dp[row][col] = minCurCellHealth(row, col)

        return dp[0][0]


# TC = O(ROWS*COLS)
# SC = O(ROWS*COLS), but possible to optimize to O(ROWS) because we only access neighbors cur_row + 1 and cur_col + 1
