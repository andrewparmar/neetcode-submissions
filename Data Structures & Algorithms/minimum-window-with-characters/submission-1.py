from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = {}

        l = 0
        need = len(count_t)
        found = 0
        res = ""
        res_length = float('inf')
        for r in range(len(s)):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                found += 1
            if found == need and res_length > (r - l + 1):
                res = s[l:r+1]
                res_lenght = len(res)
            print(count_s, found, s[l:r+1], res)

            while found == need:
                if s[l] in count_t and count_s[s[l]] == count_t[s[l]]:
                    found -= 1
                if found == need and res_length > (r - l):
                    res = s[l+1:r+1]
                    res_length = len(res)
                count_s[s[l]] = count_s[s[l]] - 1
                l += 1
    
        return res
