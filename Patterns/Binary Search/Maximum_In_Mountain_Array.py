def findPeak(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return nums[l]


if __name__ == "__main__":
    arr = [556, 45, 4, 3, 1]
    res = findPeak(arr)
    print(res)
