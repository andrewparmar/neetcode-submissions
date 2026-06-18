class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.buildDict(s)
        dict_t = self.buildDict(t)
        return dict_s == dict_t
        
    def buildDict(self, x) -> Dict:
        _dict = {}
        for ch in x:
            if ch not in _dict:
                _dict[ch] = 0
            _dict[ch] += 1
        return _dict