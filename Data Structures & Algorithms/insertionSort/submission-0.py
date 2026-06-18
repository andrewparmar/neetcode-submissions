# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        """
        maintain res
        add pairs as-is to res
        for each subsequent sort, when item is in correct position
        add pairs to res
        """
        res = []

        for j in range(len(pairs)):
            i = j
            while i > 0:
                if pairs[i].key < pairs[i-1].key:
                    pairs[i], pairs[i-1] = pairs[i-1], pairs[i]
                    i -= 1
                else:
                    break
            res.append([x for x in pairs])
            # print([(x.key, x.value) for x in pairs])
        return res
