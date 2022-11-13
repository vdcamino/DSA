# Divide: recurse until you be able to call merge on only sorted arrays
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


# Conquer: function that merges two sorted arrays
def merge(first_arr, second_arr):
    res = (
        []
    )  # output (sorted array), the merge of the two sorted arrays (first_arr, second_arr)
    i = 0  # index that will traverse the first array
    j = 0  # index that will traverse the second array
    while i < len(first_arr) and j < len(second_arr):
        if first_arr[i] <= second_arr[j]:
            res.append(first_arr[i])
            i += 1
        else:
            res.append(second_arr[j])
            j += 1
    # chain the remaining array with res
    if i == len(first_arr):  # i traversed its whole array, so chain res with j's array
        res += second_arr[j:]
    else:
        res += first_arr[i:]
    return res


if __name__ == "__main__":
    nums = [2, 5, 3, 1, 4, 5, 3, 2, 6, 7, 7, 21, 3, 7, 2, 14, 13, 23]
    res = mergesort(nums)
    print(res)
