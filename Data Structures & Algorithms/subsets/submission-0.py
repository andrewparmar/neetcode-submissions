class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # Base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include element
            subset.append(nums[i])
            dfs(i + 1)

            # Don't Include element
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res