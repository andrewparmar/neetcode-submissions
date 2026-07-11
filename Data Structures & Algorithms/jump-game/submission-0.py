class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, num in enumerate(nums):
            if i <= farthest:
                farthest = max(farthest, i + num)
            else:
                return False
        return True
