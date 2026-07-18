class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        candidates.sort()

        def backtracking(i, curr_sum):
            if curr_sum == target:
                res.append(combination.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if curr_sum + candidates[j] <= target:
                    combination.append(candidates[j])
                    backtracking(j + 1, curr_sum + candidates[j])
                    combination.pop()
            
            return

        backtracking(0, 0)

        return res
