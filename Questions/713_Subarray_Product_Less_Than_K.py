class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curProd = 1
        l = 0
        res = 0
        if k <= 1:
            return 0

        for r in range(len(nums)):
            curProd *= nums[r]

            while curProd >= k:
                curProd = curProd // nums[l]
                l += 1

            res += r - l + 1

        return res
