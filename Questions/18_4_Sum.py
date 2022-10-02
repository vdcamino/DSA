class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # eliminate duplicates

        # use recursion get generic case
        # 3 sum requires to sort the array, do ONE for loop and one while with right + left pointers
        # 4 sum requires to sort the array, do TWO for loops and one while with right + left pointers
        [-2, -2, 0, 0, 1, 2]
        # to the recursion call, pass the current k, the current index, and the current target
        res, quad = [], []
        3, 1, 6
        quad = [2, 2]

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base case, two sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[r] + nums[l] > target:
                    r -= 1
                elif nums[r] + nums[l] < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res
