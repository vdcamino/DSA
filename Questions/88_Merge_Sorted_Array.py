class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        count1 = m - 1
        count2 = n - 1
        # case m == 0
        while i < n + m:
            if count1 == -1:
                nums1[count1 + count2 + 1] = nums2[count2]
                count2 -= 1
            elif count2 == -1:
                nums1[count1 + count2 + 1] = nums1[count1]    
                count1 -= 1
            elif nums1[count1] >= nums2[count2]:
                nums1[count1 + count2 + 1] = nums1[count1]
                count1 -= 1
            else:
                nums1[count1 + count2 + 1] = nums2[count2]
                count2 -= 1
            i += 1