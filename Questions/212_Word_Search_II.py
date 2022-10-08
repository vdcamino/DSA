class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "*"
        # build trie as a hashmap of hashmaps (we could have also created a trie data structure with its own add and remove methods)
        trie = {}

        # add words to the trie
        for w in words:
            node = trie
            for letter in w:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = w

        rowNum = len(board)
        colNum = len(board[0])

        res = []

        def dfs(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # pop the matched word to avoid duplicates,
                res.append(word_match)

            # before the exploration, mark the cell as visited
            board[row][col] = "#"

            # explore the neighbors in 4 directions, i.e. up, right, down, left
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for rowOffset, colOffset in directions:
                newRow, newCol = row + rowOffset, col + colOffset
                if (
                    newRow >= 0
                    and newRow < rowNum
                    and newCol >= 0
                    and newCol < colNum
                    and board[newRow][newCol] in currNode
                ):
                    dfs(newRow, newCol, currNode)

            # end of exploration, we restore the cell
            board[row][col] = letter

            # optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    dfs(row, col, trie)

        return res
