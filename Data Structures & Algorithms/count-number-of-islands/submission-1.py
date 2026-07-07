class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(cell):
            # row, col = cell
            q = deque()
            q.append(cell)
            visited.add(cell)

            while q:
                row, col = q.popleft()
                for dr, dc in [-1, 0], [1, 0], [0, -1], [0, 1]:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visited.add((r,c))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs((row, col))
        
        return islands