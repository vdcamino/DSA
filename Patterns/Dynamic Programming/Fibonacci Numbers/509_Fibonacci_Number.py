class Solution:
    def fib(self, n: int) -> int:
        cache = [0, 1]
        if n < 2:
            return cache[n]
        for _ in range(n - 1):
            tmp = cache[1]
            cache[1] = cache[1] + cache[0]
            cache[0] = tmp
        return cache[1]
