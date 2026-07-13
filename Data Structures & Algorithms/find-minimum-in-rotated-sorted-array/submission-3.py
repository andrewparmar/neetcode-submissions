class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] >= nums[r]:
                # pivot in right
                l = m + 1
            else:
                # pivot in left
                r = m
        return nums[l]



    # def findMin(self, nums: List[int]) -> int:
    #     l, r = 0, len(nums) - 1

    #     while l < r:
    #         m = (l + r) // 2
    #         print(nums[l], nums[m], nums[r])
    #         if nums[m] >= nums[r]:
    #             # pivot in right half
    #             l = m + 1
    #         else:
    #             # pivot in left half
    #             r = m

    #     return nums[l]
