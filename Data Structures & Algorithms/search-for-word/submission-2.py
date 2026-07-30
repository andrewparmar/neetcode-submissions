class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        
        seen = set()
        def backtracking(r, c, i):
            # if i == len(word):
            #     return True
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            seen.add((r,c))

            for dr, dc in [-1, 0], [1, 0], [0, -1], [0, 1]:
                row, col = r + dr, c + dc
                if (row in range(rows) and
                    col in range(cols) and
                    (row,col) not in seen):
                    if backtracking(row, col, i + 1):
                        return True

            seen.remove((r, c))
            return False

        for row in range(rows):
            for col in range(cols):
                if backtracking(row, col, 0):
                    return True

        return False