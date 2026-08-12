class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i + 1