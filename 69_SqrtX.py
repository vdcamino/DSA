class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x <= 1:
            return x
        while (left <= right):
            mid = (left + right) // 2
            if mid ** 2 <= x  < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x: 
                right = mid - 1
            else: 
                left = mid + 1
        return mid