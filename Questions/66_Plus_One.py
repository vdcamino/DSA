class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if (digits[i] == 9):
                digits[i] = 0
                if (i == 0):
                    digits.insert(0, 1)
                    break;
                else:
                    digits[i] = 0
                    i -= 1
            else: 
                digits[i] += 1
                break;
        return digits