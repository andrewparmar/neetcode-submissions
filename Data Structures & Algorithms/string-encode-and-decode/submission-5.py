class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        list to string
        question doesn't say what encoding to use
        """
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            res.append(s[j + 1: j + 1 + count])
            i = j + 1 + count
                
        return res
            
