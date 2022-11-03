class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []

        # 0/1 napsack problem, we can choose to include the current element or not
        def backtrack(i):
            # base case
            if i == len(nums):
                # shallow copy
                res.append(curSet.copy())
                return

            # pick current node
            curSet.append(nums[i])

            backtrack(i + 1)

            # don't pick current node
            curSet.pop()
            backtrack(i + 1)

        backtrack(0)

        return res
