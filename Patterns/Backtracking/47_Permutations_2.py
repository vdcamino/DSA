class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequencies = Counter(nums)
        res = []
        curPerm = []

        def backtrack():
            if len(curPerm) == len(nums):
                res.append(curPerm.copy())
                return

            for n in frequencies:
                if frequencies[n] > 0:
                    curPerm.append(n)
                    frequencies[n] -= 1

                    backtrack()

                    curPerm.pop()
                    frequencies[n] += 1

        backtrack()
        return res
