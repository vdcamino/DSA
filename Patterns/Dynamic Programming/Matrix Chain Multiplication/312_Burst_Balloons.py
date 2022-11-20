class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # handle edge case
        nums = [1] + nums + [1]
        # memoization
        cache = {}

        def dfs(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            # initialize result as zero
            cache[(left, right)] = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                # update the result
                cache[(left, right)] = max(cache[(left, right)], coins)
            return cache[(left, right)]

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dfs(1, len(nums) - 2)
