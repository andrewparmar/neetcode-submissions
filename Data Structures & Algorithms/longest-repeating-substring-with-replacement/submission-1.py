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

        counter = defaultdict(int)
        l, r = 0, 0
        res = 0
        
        while r < len(s):
            counter[s[r]] += 1
            print(l, r, counter)
            window = r - l + 1
            if (window - max(counter.values()) <= k):
                res = max(res, window)
            else:
                while (window - max(counter.values())) > k:
                    counter[s[l]] -= 1
                    print("shrinking window", counter)
                    l += 1
                    window = r - l + 1
                    print()
            r += 1
        
        return res
