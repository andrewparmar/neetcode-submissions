class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        First binary search for the target row
        Then within the target row, serach for the target
        """
        m, n = len(matrix), len(matrix[0])

        # target row
        row = None

        t, b = 0, m - 1
        l, r = 0, n - 1

        while t <= b:
            c = (t + b) // 2
            # print(t, b, c, target)
            # print(matrix[c])
            if matrix[c][l] <= target <= matrix[c][r]:
                row = c
                break
            elif matrix[c][0] > target:
                b = c - 1
            else:
                t = c + 1

        if row is None:
            return False
        nums = matrix[row]
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False