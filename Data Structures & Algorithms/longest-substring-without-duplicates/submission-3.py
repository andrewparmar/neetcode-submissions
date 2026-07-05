class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxy
        i
           j
        """
        seen = set() # {x, y, z}
        i = 0
        longest = 0 # 1, 2, 3

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            longest = max(longest, j - i + 1)
            seen.add(s[j])
            j += 1

        return longest