class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = float("-inf")
        total = float("-inf")

        for num in nums:
            if total + num < num:
                total = num
            else:
                total += num
            _max = max(_max, total)

        return _max