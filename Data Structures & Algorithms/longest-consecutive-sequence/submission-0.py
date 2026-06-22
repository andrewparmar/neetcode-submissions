class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0 # 0 4
        for num in nums:
            if (num-1) not in s:
                streak = 0 # 0 1 2 3 4 x
                curr = num # 2 3 4 5 6
                while curr in s:
                    streak += 1 
                    curr += 1
                res = max(streak, res) 
        return res
