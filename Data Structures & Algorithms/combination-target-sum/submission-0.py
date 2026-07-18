class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def backtracking(i, curr_sum):
            if curr_sum == target:
                res.append(combination.copy())
                return

            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum <= target:
                    combination.append(nums[j])
                    backtracking(j, curr_sum)
                    combination.pop()
                curr_sum -= nums[j]
        
        backtracking(0, 0)

        return res