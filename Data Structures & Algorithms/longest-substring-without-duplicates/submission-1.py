class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use set for seen characters in the sliding window 
        zxyzxyz
        i
        j
        """
        seen = set()
        i = 0
        res = 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, j - i + 1) 

        return res
