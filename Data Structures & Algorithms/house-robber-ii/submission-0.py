class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
            dp = [0 for _ in range(len(arr))]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i])
            
            return dp[-1]
        
        if len(nums) <= 2:
            return max(nums)

        return max(helper(nums[:-1]), helper(nums[1:]))