class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = set()

        # def dfs():
        #     if len(perm) == len(nums):
        #         res.append(perm.copy())
        #         return
        #     for i in range(len(nums)):
        #         if i not in used:
        #             used.append(i)
        #             perm.append(i)
        #             dfs()
        #             perm.pop()
        #             used.remove(i)
        #     return

        # return res

        def backtracking():
            # is solution?
            if len(nums) == len(perm):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                # is options valid
                if i not in used:
                    used.add(i)
                    perm.append(nums[i])
                    backtracking()
                    perm.pop()
                    used.remove(i)
            
        backtracking()

        return res

    