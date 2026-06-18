class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for s in strs:
            _hash = self.get_hash(s)
            if _hash not in groups:
                groups[_hash] = []
            groups[_hash].append(s)

        return groups.values()

    def get_hash(self, string):
        _hash = [0] * 26
        for ch in string:
            _hash[ord(ch) - 97] += 1
        return ".".join(str(x) for x in _hash)
