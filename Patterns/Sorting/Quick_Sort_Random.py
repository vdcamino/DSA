def quicksort(arr, left, right):
    # base case
    if left >= right:
        return

    i, j = left, right

    pivot = arr[random.randint(left, right)]

    while i <= j:
        # i searches for an element greater than pivot
        while arr[i] < pivot:
            i += 1
        # j searches for an element smaller than pivot
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # recurse with new boudaries as left and right crossed each other
    quicksort(arr, left, j)
    quicksort(arr, i, right)
