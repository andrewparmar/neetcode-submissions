class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[r]:
                # pivot in right half
                l = l + 1
            else:
                # pivot in left half
                r = m

        return nums[l]