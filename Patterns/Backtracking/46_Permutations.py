class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curPerm = []

        def backtrack():
            # base case
            if len(curPerm) == len(nums):
                res.append(curPerm.copy())
                return

            for i in range(len(nums)):
                # append to the permutation the next element that is not already taken
                if nums[i] not in curPerm:
                    curPerm.append(nums[i])
                    backtrack()
                    # backtrack removing last inserted element and continue permutation from i + 1
                    curPerm.pop()

        backtrack()
        return res


# TC = O(n x n!) instead of O(n!), since you will have n! permutations. And, for each permutation, you run exact n recursive call to reach it.
# SC = O(n!)
