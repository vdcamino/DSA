class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        right = sum(nums)
        left = max(nums)
        # left-biased binary search
        while left < right:
            mid = left + (right - left) // 2
            valid = True
            # try to get a split with sum at maximum = mid
            i, curSum, curK = 0, 0, k
            while i < len(nums):
                curSum += nums[i]
                if curSum > mid:
                    if curK == 1:
                        valid = False
                        break
                    else:
                        curSum = nums[i]
                        curK -= 1
                i += 1
            # try to shrink if partition is valid
            if valid:
                right = mid
            else:
                left = mid + 1
        return left
