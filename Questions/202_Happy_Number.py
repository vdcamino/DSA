class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, k):
        output = 0

        while k:
            digit = k % 10
            output += digit**2
            k = k // 10

        return output
