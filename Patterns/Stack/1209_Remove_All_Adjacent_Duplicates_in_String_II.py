class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count], use list so we can change count
        for i in range(len(s)):
            # if current char is equal to previous char, increment count
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            # else start new streak
            else:
                stack.append([s[i], 1])

            # check if we hit the limit, if yes we need to remove
            if stack[-1][1] == k:
                stack.pop()

        # build return string
        res = []
        for i in range(len(stack)):
            # could have multiplied strings also: res = "" then res += stack[i][0]*stack[i][1]
            for _ in range(stack[i][1]):
                res.append(stack[i][0])

        return "".join(res)
