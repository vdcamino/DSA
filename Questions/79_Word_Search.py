class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # visited flag = '*'

        def dfs(r, c, i):
            # found the last character of our word
            if i == len(word):
                return True
            # check if this is not a valid path
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or board[r][c] != word[i]:
                return False

            # mark char as visited
            temp = board[r][c]
            board[r][c] = "*"

            # all possible direcitons (up, dowm, left and right)
            res = (
                dfs(r - 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r + 1, c, i + 1)
            )

            board[r][c] = temp
            return res

        # try to find the word starting from every position of the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
