from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        first need a count of each integer
        then sort by count and return top K.
        """ 
        ## nlog(n) - why??
        # counter = defaultdict(lambda: 0)
        # for num in nums:
        #     counter[num] += 1
        # sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # return [x[0] for x in sorted_counts[:k]]

        # Bucket sort
        # counter = defaultdict(int)
        # for num in nums:
        #     counter[num] += 1
        # buckets = [[] for _ in range(len(nums) + 1)]
        # for i, freq in counter.items():
        #     buckets[freq].append(i)
        
        # res = []
        # for freq in reversed(buckets):
        #     for x in freq:
        #         res.append(x)
        #         if len(res) == k:
        #             return res

        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)

        res = []
        for x in reversed(buckets):
            for i in x:
                res.append(i)
                if len(res) == k:
                    return res

