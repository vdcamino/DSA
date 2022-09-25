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


from collections import deque


def calcMaxLenght(processPower, bootPower, maxPower):
    res = 0
    l, r = 0, 0
    sumVal = 0  # Help store the cumulative sum in the sliding window
    window = deque()  # Help extract max value in the sliding window

    while r < len(bootPower):
        # Clear smaller values before appending the new value
        while window and window[-1] < bootPower[r]:
            window.pop()
        # Append new value, expand the sliding window
        window.append(bootPower[r])
        # Get the max val in the curr sliding window from deque
        maxVal = window[0]
        sumVal += processPower[r]
        r += 1  # Move forward the right pointer
        consmp = maxVal + sumVal * (r - l)

        # Shrink the window when consmp bigger than the threshold
        while consmp > maxPower:
            # Pop the left element from deque
            # If head of deque isn't equal to lth element, it means that lth element is already popped out
            if window[0] == bootPower[l]:
                window.popleft()
            maxVal = window[0]
            sumVal -= processPower[l]
            l += 1  # Move forward the left pointer
            consmp = maxVal + sumVal * (r - l)

        # Consmp is no bigger than the powerMax, satisfying the condition, update the max length
        res = max(res, r - l)

    return res  # The result


def main():

    bootingPower = [3, 6, 1, 3, 4]
    processPower = [2, 1, 3, 4, 5]
    powerMax = 25
    maxLength = calcMaxLenght(processPower, bootingPower, powerMax)
    print(maxLength)


if __name__ == "__main__":
    main()
