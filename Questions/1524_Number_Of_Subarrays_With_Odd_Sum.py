class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # dp of size two if going to store at
        # dp[0] = the number of even subarrays
        # dp[1] = the number of even subarrays
        # Note: dp[0] is initialized as one because a single
        # odd element is also considered as a subarray
        dp = [1, 0]
        # run is the current sum under modulo 2 and ending at index i
        res, run = 0, 0

        # each iteration computes the sum of arr[0:i + 1] under modulo 2
        # and increments the even/odd count according to run's value
        for n in arr:
            # 2 is added to handle the case of negative numbers
            run = (((run + n) % 2) + 2) % 2

            # increment even/odd count
            dp[run] += 1

        # an odd number can be formed by and even-odd pair
        res = dp[0] * dp[1]

        return res % (10**9 + 7)
