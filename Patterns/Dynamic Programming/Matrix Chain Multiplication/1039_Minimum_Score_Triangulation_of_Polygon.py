class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        cache = {}

        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            cache[(left, right)] = +inf
            for i in range(left + 1, right):
                score = (
                    values[left] * values[right] * values[i]
                    + dfs(left, i)
                    + dfs(i, right)
                )
                cache[(left, right)] = min(cache[(left, right)], score)
            return cache[(left, right)]

        return dfs(0, len(values) - 1)
