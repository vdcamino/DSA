class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Optimization 1: verify if board has the minimum number of characters
        if len(word) > ROWS * COLS:
            return False

        # Optimization 2: verify if board has all the characters of the word
        board_dict = defaultdict(int)
        for row in range(ROWS):
            for col in range(COLS):
                board_dict[board[row][col]] += 1
        # Count frequency of letters in word
        wordDic = Counter(word)
        for c in wordDic:
            if board_dict[c] < wordDic[c]:
                return False

        # DFS with backtracking
        def dfs(row, col, i):
            # Base case 1
            if i == len(word):
                return True
            # Base case 2
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or board[row][col] != word[i]
            ):
                return False

            # Mark cell as visited
            temp = board[row][col]
            board[row][col] = "*"

            # Explore all the 4 possible directions
            for row_offset, col_offset in DIRECTIONS:
                new_row, new_col = row + row_offset, col + col_offset
                if dfs(new_row, new_col, i + 1):
                    return True

            # Backtrack reestablishing original board
            board[row][col] = temp

            return False

        # Try to find the word starting from every position of the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        # If after exploration no dfs returned True, the word is not present in the grid
        return False
