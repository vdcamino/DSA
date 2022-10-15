class Solution:
    def checkValidString(self, s: str) -> bool:
        balance_min = 0  # minimum balance we can have
        balance_max = 0  # maximum balance we can have
        for c in s:
            if c == ")":
                balance_min -= 1
                balance_max -= 1
            elif c == "(":
                balance_min += 1
                balance_max += 1
            else:
                balance_min -= 1
                balance_max += 1

            # if our maximum balance is less than zero, it means we didn't have enough opens to match the closing parenthesis that we have encountered
            if balance_max < 0:
                return False

            # If balance_min drops below 0 and then gets back to 0, it means we "borrowed" future '('s. In other words, a ')' was encountered before a matching '('
            # Simplest example is "*("
            if balance_min < 0:
                balance_min = 0

            # Return true if at the end we can find balance == 0 (it must be in range balance_min, open_closed)
            # It will be the case only if open min is zero
            # because if open min is 1+ we know that we can only have open counts of 1, 2, 3...
        return balance_min == 0
