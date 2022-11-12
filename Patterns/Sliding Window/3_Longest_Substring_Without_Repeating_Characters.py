class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        count_char = defaultdict(int)
        max_length = -inf

        # sliding window
        l = 0
        for r in range(len(s)):
            count_char[s[r]] += 1
            while count_char[s[r]] > 1:
                count_char[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
