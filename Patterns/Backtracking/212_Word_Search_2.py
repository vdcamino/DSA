class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        ROWS, COLS = len(board), len(board[0])
        WORD_KEY = "%"
        res = []

        # Fill up the trie with the words from input
        trie = TrieNode()
        for word in words:
            ptr = trie
            for c in word:
                if c not in ptr.children:
                    ptr.children[c] = TrieNode()
                ptr = ptr.children[c]
            # Optimization 1: store word in the trie so we don't need to pass current prefix to each recursive call and then build word if node is end of word
            ptr.children[WORD_KEY] = word

        # backtracking/dfs
        def dfs(cur_row, cur_col, parent):
            cur_letter = board[cur_row][cur_col]
            cur_node = parent.children[cur_letter]

            # Optimization 2: retrieve matching word + set flag to then prune current node since it is a leaf node of a matched word
            word_match = cur_node.children.pop(WORD_KEY, False)
            if word_match:
                res.append(word_match)

            # Mark cell as visited
            board[cur_row][cur_col] = "#"

            # Explore all 4 possible directions
            for row_offset, col_offset in DIRECTIONS:
                new_row, new_col = cur_row + row_offset, cur_col + col_offset
                if (
                    new_row in range(ROWS)
                    and new_col in range(COLS)
                    and board[new_row][new_col] in cur_node.children
                ):
                    dfs(new_row, new_col, cur_node)

            # Reestablish visited cell
            board[cur_row][cur_col] = cur_letter

            # Optimization 2: prune leaf node of matched word
            if not cur_node.children:
                parent.children.pop(cur_letter)

        # Dfs/backtrack every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.children:
                    dfs(r, c, trie)

        return res
