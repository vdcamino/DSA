# Remove any equal char streak (direct or indirect)
# adbbbdc --> ac
# adddddbbbddc --> ac


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # [char, count]
        # identify adjecent repeated chars
        for i in range(len(s)):
            if not stack or stack[-1][0] != s[i]:
                stack.append([s[i], 1])
            else:
                stack[-1][1] += 1

        # identify flags (taking into account repeated/indirect streaks)
        flags = set()
        for i in range(len(stack)):
            if stack[i][1] != 1:
                # mark all elements belonging to the palindrome as flags to not include in final result
                flags.add(i)
                l, r = i - 1, i + 1
                while l >= 0 and r < len(stack) and stack[l][0] == stack[r][0]:
                    # merge two sets
                    flags |= set([l, r])
                    l -= 1
                    r += 1

        # build final result avoiding chars marked as flags
        res = []
        for i in range(len(stack)):
            if i not in flags:
                res.append(stack[i][0])

        return "".join(res)
