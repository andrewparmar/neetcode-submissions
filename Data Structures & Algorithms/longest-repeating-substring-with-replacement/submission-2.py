from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        use 2 ptrs. Check that second pointer char == first pointer.
        While k attempts remain, decrease k and increase j by 1.
        Keep track of first character changed
        When k runs out, reset right pointer to saved spot.

        This might be the brute force approach
        """

        counter = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            while (r - l + 1  - max(counter.values())) > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res