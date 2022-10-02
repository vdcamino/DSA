def greatestMovieComb(myArray, maxAllowed):
    # sort in descending order
    list_keep_init_index = list(zip([i for i in range(len(myArray))], myArray))
    list_keep_init_index = sorted(
        list_keep_init_index, key=lambda x: x[1], reverse=True
    )
    # binary search to find the optimal pair of values
    # the goal is to walk the last possible towards the right, and so use the max left possible in the final comb
    left = 0
    right = len(list_keep_init_index) - 1
    curr_max = -1
    res = [[-1, -1], [-1, -1]]
    while left < right:
        curr_sum = list_keep_init_index[left][1] + list_keep_init_index[right][1]
        print(curr_sum)
        if (
            curr_sum > curr_max
            or (
                curr_sum == curr_max
                and max(list_keep_init_index[left][1], list_keep_init_index[right][1])
                > max(res[0][1], res[1][1])
            )
        ) and curr_sum <= maxAllowed:
            curr_max = curr_sum
            res[0] = list_keep_init_index[left]
            res[1] = list_keep_init_index[right]
        if curr_sum > maxAllowed:
            left += 1
        else:
            right -= 1
    return res


if __name__ == "__main__":
    myArray = [27, 1, 10, 39, 12, 52, 32, 67, 76]
    print(greatestMovieComb(myArray, 77))
