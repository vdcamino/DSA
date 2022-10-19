from cmath import inf


def findPeak(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    ans = -inf
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > ans:
            ans = nums[mid]
        if nums[mid] > nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return ans


if __name__ == "__main__":
    arr = [0, 4, 9, 12, 34, 556, 678]
    res = findPeak(arr)
    print(res)
