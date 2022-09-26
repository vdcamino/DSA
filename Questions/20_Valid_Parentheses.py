class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        # traverse string from right to left
        for c in s:
            if c in closeToOpen:
                # if it is a closing char, we need to have its compliment at the top of the stack
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return True if not stack else False
