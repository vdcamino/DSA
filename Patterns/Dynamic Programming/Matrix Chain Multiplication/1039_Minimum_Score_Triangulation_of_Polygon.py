class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        cache = {}

        # function the gets the minimum possible triangulation score
        # with left and right (included) as two of the bounds
        def dfs(left, right):
            # base case
            if right - left + 1 < 3:
                return 0
            # memoization
            if (left, right) in cache:
                return cache[(left, right)]

            # initiate result variable that we want to minimize
            cache[(left, right)] = +inf
            # for each element between left and right, consider it as the third vertex
            for i in range(left + 1, right):
                # calculate triangulation score for this vertex
                score = (
                    values[left] * values[right] * values[i]
                    + dfs(left, i)
                    + dfs(i, right)
                )
                # try to update score for these bounds
                cache[(left, right)] = min(cache[(left, right)], score)
            return cache[(left, right)]

        return dfs(0, len(values) - 1)
