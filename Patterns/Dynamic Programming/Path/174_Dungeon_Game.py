class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dp = [[+inf for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        # helper function to compare decision between right and down
        def get_min_health(cell_damage, nei_row, nwi_col):
            next_health = dp[nei_row][nwi_col]
            # hero needs at least 1 point to survive
            return max(1, next_health - cell_damage)

        # traverse the dungeon starting from the end (bottom up)
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                cur_damage = dungeon[row][col]

                down_health = get_min_health(cur_damage, row + 1, col)
                right_health = get_min_health(cur_damage, row, col + 1)
                cur_health = min(down_health, right_health)

                # you cannot accumulate health in this game
                if cur_health == +inf:
                    cur_health = 1 if cur_damage >= 0 else (1 - cur_damage)

                dp[row][col] = cur_health

        return dp[0][0]


# TC = O(ROWS*COLS)
# SC = O(ROWS*COLS), but possible to optimize to O(ROWS) because we only access neighbors cur_row + 1 and cur_col + 1
