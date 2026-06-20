import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = 1
        i = 0
        res = []
        while i < len(nums):
            # calculate left
            # calculate right
            # prod left*right for res at index i
            l_prod = math.prod(nums[:i]) if i != 0 else 1
            r_prod = math.prod(nums[i+1:]) if i != len(nums) - 1 else 1
            res.append(l_prod * r_prod)
            i += 1
        return res