class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        maxLength = 1

        for n in nums:
            if not n - 1 in nums:
                curLength = 1
                # it is the start of a sequence
                while n + 1 in nums:
                    curLength += 1
                    maxLength = max(maxLength, curLength)
                    n = n + 1

        return maxLength
