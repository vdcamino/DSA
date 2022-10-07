class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res, prefix, l, distinctCount = 0, 0, 0, 0
        freq = {}

        for r in range(len(nums)):

            # check if this new number is distinct or not
            if nums[r] not in freq or freq[nums[r]] == 0:
                distinctCount += 1
                freq[nums[r]] = 1
            else:
                freq[nums[r]] += 1

            # window is invalid, shrink once to try to make it valid again (the next while loop will make it valid if this one does not)
            if distinctCount > k:
                prefix = 0
                freq[nums[l]] -= 1
                distinctCount -= 1
                l += 1

            # keep track of the number of duplicates on the left of the window
            while freq[nums[l]] > 1:
                freq[nums[l]] -= 1
                prefix += 1
                l += 1

            if distinctCount == k:
                res += prefix + 1
        return res


#         return self.atMost(nums, k) - self.atMost(nums, k - 1)

#     def atMost(self, arr, d):
#         if d < 1:
#             return 0
#         freq = {}
#         l, res, distinctNumbers = 0, 0, 0
#         for r in range(len(arr)):
#             if arr[r] in freq:
#                 freq[arr[r]] += 1
#             else:
#                 freq[arr[r]] = 1
#                 distinctNumbers += 1
#             while distinctNumbers > d:
#                 freq[arr[l]] -= 1
#                 if freq[arr[l]] == 0:
#                     distinctNumbers -= 1
#                     del freq[arr[l]]
#                 l += 1
#             res += r - l + 1
#         return res
