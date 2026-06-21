class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        s_nums = sorted(nums)
        i = 0
        prev_nums_i = None
        while i <= (len(nums) - 3):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                i += 1
                continue
            t = 0 - s_nums[i]
            j, k = i + 1, len(nums) - 1
            print(i, j, k)
            print(s_nums[i], s_nums[j], s_nums[k])
            while j < k:
                _sum = s_nums[j] + s_nums[k]
                if _sum == t:
                    res.append([s_nums[i], s_nums[j], s_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and s_nums[j] == s_nums[j-1]:
                        j += 1
                    while j < k and s_nums[k] == s_nums[k+1]:
                        k -= 1
                elif _sum < t:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res
                