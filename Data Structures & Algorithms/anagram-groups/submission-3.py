from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Same characters and count.
        Need to create a consistent encoding
        letterNumber pairs as a list
        """ 
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())
