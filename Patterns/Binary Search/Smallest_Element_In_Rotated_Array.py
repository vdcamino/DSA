from cmath import inf


def findSmallest(arr):
    if not arr:
        return -1
    res = +inf
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < res:
            res = arr[mid]
        if arr[mid] <= arr[r]:
            r = mid - 1
        else:
            if arr[l] < res:
                res = arr[l]
            l = mid + 1

    return res


if __name__ == "__main__":
    nums = [6, 7, 9, 15, 19, 0, 2, 3, 5]
    ans = findSmallest(nums)
    print(ans)
