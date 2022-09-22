# given a list of servers
# input 1 -> process_pow [1, 9, 3, 0]
# input 2 -> boot_pow [2, 4 3, 3]

# Give you a list servers. Their processing power is given as a array of integer, and boot power as a array of integer.
# Write a function to return the max length of sub array which's power consumption is less than or equal to max power limit.
# Formula to calculate the power consumption for a subArray is:
# Max(bootPower[i...j]) + Sum(processPower[i....j]) * length of subArray.

# Note: Single server is also a subArray, return 0 if no such subArray can be found.

# public int MaxLengthValidSubArray(int[] processingPower, int[] bootingPower, int maxPower)
# {}

# find largest sum with sliding window


def func(pp, bp, max_allowed):
    # base cases
    if not bp or not pp:
        return 0
    # create one single list for the powers
    power = [x + y for x, y in zip(bp, pp)]
    length = len(bp)
    if length == 1:
        if power[0] < max_allowed:
            return 1
        else:
            return 0
    # sliding window
    l, r = 0, 1
    max_coor = [-1, -1]  # keep track of the coordinates the extremities of our curr max
    curr_max = -1
    curr_sum = power[r] + power[l]
    while l < length:
        curr_pow = curr_sum * (r - l + 1)
        # curr_power equal to target
        if curr_pow == max_allowed:
            return max_coor[1] - max_coor[0] + 1
        # if left equal to right or curr power is less than max allowed
        elif l == r and r != length - 1:
            r += 1
            curr_sum += bp[r] + pp[r]
        # current power less than target
        # try to push right further right
        elif curr_pow < max_allowed:
            r += 1
            curr_sum += bp[r] + pp[r]
            # verify if we have found a new max
            if curr_max < curr_pow:
                curr_max = curr_pow
                max_coor = [l, r]
        # current power greater than target, need to reduce the sum
        elif curr_pow > max_allowed or r == length - 1:
            curr_sum -= bp[l] + pp[l]
            l += 1
    if max_coor[0] == -1:
        return 0
    return max_coor[1] - max_coor[0] + 1
