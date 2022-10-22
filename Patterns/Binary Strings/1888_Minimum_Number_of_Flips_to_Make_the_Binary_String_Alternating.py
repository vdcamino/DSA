class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        mismatches_start_0 = 0  # supposing 0 at even indexes
        mismatches_start_1 = 0  # supposing 1 at even indexes
        res = +inf

        l = 0
        for r in range(2 * n):
            if r % 2:
                if s[r % n] == "0":
                    mismatches_start_0 += 1
                else:
                    mismatches_start_1 += 1
            else:
                if s[r % n] == "0":
                    mismatches_start_1 += 1
                else:
                    mismatches_start_0 += 1

            if r >= n:
                if l % 2:
                    if s[l] == "0":
                        mismatches_start_0 -= 1
                    else:
                        mismatches_start_1 -= 1
                else:
                    if s[l] == "0":
                        mismatches_start_1 -= 1
                    else:
                        mismatches_start_0 -= 1
                l += 1

            if r - l + 1 == n:
                res = min(res, mismatches_start_1, mismatches_start_0)

        return res
