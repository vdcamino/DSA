class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos = self.binSearch(nums, target, True)
        last_pos = self.binSearch(nums, target, False)
        return [first_pos, last_pos]

    def binSearch(self, arr, target, leftBias):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                res = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return res
