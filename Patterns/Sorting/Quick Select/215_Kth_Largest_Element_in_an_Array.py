class Solution:
    def findKthLargest(self, nums, k):
        # Kth largest element is also the len(nums) - k smallest element
        target_pivot_idx = len(nums) - k

        # Function to place the rightmost element of the array at its correct index
        def partition(l, r):
            p, pivot_idx = l, r
            for i in range(l, r):
                if nums[i] <= nums[pivot_idx]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[pivot_idx] = nums[pivot_idx], nums[p]
            return p

        # Iterative for better space complexity
        left, right = 0, len(nums) - 1
        while True:
            p = partition(left, right)
            if p == target_pivot_idx:
                return nums[p]
            if p > target_pivot_idx:
                right = p - 1
            else:
                left = p + 1
