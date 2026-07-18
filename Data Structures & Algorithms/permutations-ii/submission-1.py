class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = set()
        nums.sort()

        def backtracking():
            # is solution?
            if len(nums) == len(perm):
                res.append(perm.copy())
                return

            prev = None 
            for i in range(len(nums)):
                # is options valid
                if i not in used and nums[i] != prev:
                    used.add(i)
                    perm.append(nums[i])
                    backtracking()
                    perm.pop()
                    used.remove(i)
                    prev = nums[i]
            
        backtracking()

        return res