def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recurse
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0  # index of the left array
        j = 0  # index of the right array
        k = 0  # index of the sorted array

        # append smallest element between left and right to the resulting array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # append the remaining items (that are already sorted) to the resulting array
        if i < len(left_arr):
            arr[k:] = left_arr[i:]
        else:
            arr[k:] = right_arr[j:]

    return arr


if __name__ == "__main__":
    input_arr = [1, 0, 2, -4, 9, 1, 0, 5, 0, 3, 1]
    res = merge_sort(input_arr)
    print(res)
