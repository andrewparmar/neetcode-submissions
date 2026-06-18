class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1

        def dfs(r, c, visited):
            if (min(r, c) < 0 or r > ROWS or c > COLS or grid[r][c] == 1 or (r, c) in visited):
                return 0
            if (r, c) == (ROWS, COLS):
                return 1

            visited.add((r, c))

            count = 0
            count += dfs(r - 1, c, visited)
            count += dfs(r + 1, c, visited)
            count += dfs(r, c - 1, visited)
            count += dfs(r, c + 1, visited)

            visited.remove((r, c))
            return count
        
        return dfs(0, 0, visit)