# To get wiggle sort, we want to order the numbers in a way such that
# (1) elements smaller than the 'median' are put into the last even slots
# (2) elements larger than the 'median' are put into the first odd slots
# (3) the medians are put into the remaining slots.


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # helper function to find the nth smallest element. Iterative quickselect
        def nsmallest(n):
            start, end = 0, len(nums) - 1
            while True:
                pivot = nums[random.randint(start, end)]
                store_idx, left, right = start, start, end
                while left <= right:
                    if nums[left] < pivot:
                        nums[store_idx], nums[left] = nums[left], nums[store_idx]
                        left += 1
                        store_idx += 1
                    elif nums[left] > pivot:
                        nums[left], nums[right] = nums[right], nums[left]
                        right -= 1
                    else:
                        left += 1

                if store_idx <= n - 1 <= right:
                    return pivot
                elif n - 1 < store_idx:
                    end = store_idx - 1
                else:
                    start = store_idx + 1

        # find median
        n = len(nums)
        median = nsmallest((n + 1) // 2)

        # helper function to calculate virtual index for wiggle sort
        mapIdx = lambda i: (1 + 2 * i) % (n | 1)

        # traverse array placing numbers in a wiggle manner
        left, right, i = 0, n - 1, 0
        while i <= right:
            if nums[mapIdx(i)] > median:
                nums[mapIdx(i)], nums[mapIdx(left)] = (
                    nums[mapIdx(left)],
                    nums[mapIdx(i)],
                )
                i += 1
                left += 1
            elif nums[mapIdx(i)] < median:
                nums[mapIdx(i)], nums[mapIdx(right)] = (
                    nums[mapIdx(right)],
                    nums[mapIdx(i)],
                )
                right -= 1
            else:
                i += 1
