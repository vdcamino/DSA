class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make sure that nums1 is the smallest array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        totalSize = len(nums1) + len(nums2)
        half = totalSize // 2

        l, r = 0, len(nums1) - 1
        while True:
            smallIndex = l + (r - l) // 2
            largeIndex = half - smallIndex - 2

            smallLeft = nums1[smallIndex] if smallIndex >= 0 else -inf
            smallRight = nums1[smallIndex + 1] if smallIndex + 1 < len(nums1) else +inf
            largeLeft = nums2[largeIndex] if largeIndex >= 0 else -inf
            largeRight = nums2[largeIndex + 1] if largeIndex + 1 < len(nums2) else +inf

            if smallLeft <= largeRight and largeLeft <= smallRight:
                # valid partition
                if totalSize % 2:
                    # odd array
                    return min(smallRight, largeRight)
                # even arr
                return (max(smallLeft, largeLeft) + min(smallRight, largeRight)) / 2
            elif smallLeft > largeRight:
                r = smallIndex - 1
            else:
                l = smallIndex + 1

        # Time Complexity = O(log(min(nums1, nums2))
        # Time Complexity = O(1)
