# Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id
# and the second integer represents a value. Your task is to find an element from a and an element form b
# such that the sum of their values is less or equal to target and as close to target as possible.
# Return a list of ids of selected elements. If no pair is possible, return an empty list.

# Example 1:

# Input:
# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7

# Output: [[2, 1]]

# Explanation:
# There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
# Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
# Example 2:

# Input:
# a = [[1, 3], [2, 5], [3, 7], [4, 10]]
# b = [[1, 2], [2, 3], [3, 4], [4, 5]]
# target = 10

# Output: [[2, 4], [3, 2]]

# Explanation:
# There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
# Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
# These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
# Example 3:

# Input:
# a = [[1, 8], [2, 7], [3, 14]]
# b = [[1, 5], [2, 10], [3, 14]]
# target = 20

# Output: [[3, 1]]
# Example 4:

# Input:
# a = [[1, 8], [2, 15], [3, 9]]
# b = [[1, 8], [2, 11], [3, 12]]
# target = 20

# Output: [[1, 3], [3, 2]]


# sort both input list base on the value --> sorted(a, lambda x : x[1]), sorted(b, lambda x:x[1])
# left pointer starting at the beginning of list_1 and right pointer starting at the end of list_2
# if the element of list_2 (the one pointed by the right pointer) exceeds the target already with the left most value of the list_1, the we can discard him
import math


def optimal_pairs(list_1, list_2, target):
    list_1.sort(key=lambda x: x[1])
    list_2.sort(key=lambda y: y[1])
    curMax = -math.inf
    res = list()
    l, r = 0, len(list_2) - 1
    # left and right pointers, starting left in the start of list_1 and right at the end of list_2
    # this is optimal because if the right most element of list_2 + left most element of list_1 > target, than the right most element of list_2 can be discarded
    while r > -1 and l < len(list_1):
        curSum = list_1[l][1] + list_2[r][1]
        if curSum >= curMax and curSum <= target:
            if curSum == curMax:
                res.append([list_1[l][0], list_2[r][0]])
            elif curSum > curMax:
                res = []
                res.append([list_1[l][0], list_2[r][0]])
                curMax = curSum
            r -= 1
            # now push right pointer to the left until we find a new value, otherwhise we could be adding duplicates to the list
            while r > -1 and list_2[r][1] == list_2[r + 1][1]:
                r -= 1
        l += 1

    if curMax == -1:
        res = [[]]

    return res


def main():
    a = [[1, 8], [2, 15], [3, 9]]
    b = [[1, 8], [2, 11], [3, 12]]
    target = 20
    ans = optimal_pairs(a, b, target)
    print(ans)


if __name__ == "__main__":
    main()
