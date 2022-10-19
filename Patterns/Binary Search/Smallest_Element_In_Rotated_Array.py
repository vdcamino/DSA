def findSmallest(arr):
    if not arr:
        return -1
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] < arr[r]:
            r = mid
        else:
            l = mid + 1
    return arr[l]


if __name__ == "__main__":
    nums = [6, 7, 9, 15, 19, 2, 3, 5]
    ans = findSmallest(nums)
    print(ans)
