# first try = putting zeros at the end and ones at the beginning
# second try = opposite
# return the min between the swaps needed between the two approaches

# suppose we are sorting zeros to the left
# for each new zero that we find in our array, we need to count the number of
# operations it would take to bring this zero to the last incorrect index in our array
# [0, 0, 1, 0]  -->  in this case, the last incorrect index is equal to 2
# everytime we find a target in the right place, we need to increment by one the last incorrect index
# we need to count the number of operations it will take to bring the 0 from the wrong index to the next currect index
def min_swaps(my_list):
    def count_swaps_to_left(target):
        last_incorrect_index = 0  # index where you can put of the last element that is
        swaps = 0
        for i in range(len(my_list)):
            if my_list[i] == target:
                # we calculate how many swaps it would take to bring this 0 till the last incorrect index
                swaps += (
                    i - last_incorrect_index
                )  # we know that the last incorrect index will have the good index of the last one becuase we only increment last_incorrect_index when we find target
                last_incorrect_index += 1
                # so if we continune traversing our array NOT findinf the target, the last_incorrect_index will have the value of the first incorrect index we have encountered
        return swaps

    return min(count_swaps_to_left(1), count_swaps_to_left(0))


def main():
    input = [0, 0, 1, 0, 1, 0]

    ans = min_swaps(input)
    print(ans)


if __name__ == "__main__":
    main()
