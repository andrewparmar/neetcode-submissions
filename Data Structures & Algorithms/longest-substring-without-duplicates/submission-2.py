class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, j = 0, 0

        longest = 0
        for j in range(len(s)):
            if s[j] in seen:
                while i < j and s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            longest = max(longest, j - i + 1)
            seen.add(s[j])

        return longest
