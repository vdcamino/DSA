# Consider an array of size n with all initial values as 0.
# Perform the given ‘m’ add operations from index ‘a’ to ‘b’
# and evaluate the highest element in the array.
# An add operation adds 100 to all elements from a to b (both inclusive).

# Approach:
# 1 : Run a loop for 'm' times, inputting 'a' and 'b'.
# 2 : Add 100 at index 'a-1' and subtract 100 from index 'b'.
# 3 : After completion of 'm' operations, compute the prefix sum array.
# 4 : Scan the largest element of the prefix sum array.

# Adding 100 only to the a index insures that all the elements from a to b will have
# +100 added when prefix sum array is calculated
# Removing 100 from b index insures that all the elements from b index onwards will have
# -100 reduced when prefix sum array is calculated


def find(m, q):
    mx = 0
    pre = [0 for i in range(5)]

    for i in range(m):
        # take input a and b
        a, b = q[i][0], q[i][1]

        # add 100 at first index and
        # subtract 100 from last index

        # pre[1] becomes 100
        pre[a - 1] += 100

        # pre[4] becomes -100 and this
        pre[b] -= 100

        # continues m times as we input diff. values of a and b
    for i in range(1, 5):

        # add all values in a cumulative way
        pre[i] += pre[i - 1]

        # keep track of max value
        mx = max(mx, pre[i])
    return mx


# Driver Code
m = 3
q = [[2, 4], [1, 3], [1, 2]]

# Function call
print(find(m, q))
