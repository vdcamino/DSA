class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            [1, "I"],
            [4, "IV"],
            [5, "V"],
            [9, "IX"],
            [10, "X"],
            [40, "XL"],
            [50, "L"],
            [90, "XC"],
            [100, "C"],
            [400, "CD"],
            [500, "D"],
            [900, "CM"],
            [1000, "M"],
        ]
        res = ""
        # traverse the roman list in reversed order (always try to put the biggest value)
        for val, sym in reversed(romans):
            # if cur roman symbol fits into the cur number
            if num // val:
                # check how many times we can put it in there
                count = num // val
                # in Python you can multiply strings to put multiple occurences of that string
                res += count * sym
                # continue the loop with the rest of current number // total value that we have appended
                num %= count * val
        return res
