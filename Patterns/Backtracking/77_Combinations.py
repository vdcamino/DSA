class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb = []

        def backtrack(first):
            # base case
            if len(curComb) == k:
                output.append(curComb[:])
                return
            for i in range(first, n + 1):
                # add i into the current combination
                curComb.append(i)
                # use next integers to complete the combination
                backtrack(i + 1)
                # backtrack
                curComb.pop()

        output = []
        backtrack(1)
        return output
