class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down memoization
        cache = {}

        def dfs(i, j):
            # memoization check
            if (i, j) in cache:
                return cache[(i, j)]

            # base cases
            # we reach the end of both strings at the same time
            if i >= len(s) and j >= len(p):
                return True
            # there is no more manipulation to be done with p string,
            # return False because there are still characters to match in s string
            if j >= len(p):
                return False

            # verify if s[i] and p[j] can be a match
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # check options with p[j + 1] == "*":
            # 1. s[i] != p[j], so choose to use p[j] zero times
            # 2. s[i] == p[j] so study branch where you use p[j] multiple times
            if (j + 1) < len(p) and p[j + 1] == "*":
                # don't use p string char OR use p string char more than once
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            # if you have a match, a new branch will be simply moving forward the two pointers
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # if you don't have a match or i is out of bounds and no p[j + 1] = "*", return False
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
