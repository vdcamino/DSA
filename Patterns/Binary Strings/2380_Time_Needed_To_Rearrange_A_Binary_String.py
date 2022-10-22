# The final string will be of the form 1111....000....

# One observation is that since a '1' has to be swapped with every occurence of '0' to its left, the time taken for that '1' to reach its final position is at least the number of zeroes to its left.

# Why is it not equal to number of '0's to its left ?
# In a testcase like '011' -> '101' -> '110', the second '1' had to wait for the first '1' in the first turn.

# The total number of time taken for a '1' to reach its final position is number of '0's to its left + number of turns it waits.

# Everytime we come across two consequetive ones, the waiting time increases by one.

# And everytime we come acress two consecutive zeroes, the waiting time decreases by one.

# Consider 0 1 1 0 0 1 the waiting time for the first '1' is 0, for the second '1' is 1 , but for the third '1' is again 0, because while the second '1' was waiting, the third '1' would not waste a turn by moving through the zeroes before it.

# Also, it is obvious that the last occurence of a '1' is the one that will reach its destination the last.

# So we just have to find the number of zeroes to the left of it + its waiting time


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        waitingTime = zeroCount = 0
        lastOcc = s.rfind("1")

        for i in range(lastOcc + 1):
            # increase waiting time if we come across 2 conseq 1's
            # however, if there are no zeroes to the left, then there is no waiting time
            if i > 0 and s[i] == "1" and s[i - 1] == "1" and zeroCount > 0:
                waitingTime += 1

            # decrease waiting time if we come across 2 conseq 0's
            if i > 0 and s[i] == "0" and s[i - 1] == "0" and waitingTime > 0:
                waitingTime -= 1

            if s[i] == "0":
                zeroCount += 1

        return zeroCount + waitingTime


# Time Complexity: O(n)
# Space Complexity: O(1)
