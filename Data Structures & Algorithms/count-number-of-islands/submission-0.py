class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid:
            return islands

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for dr, dc in [[-1,0],[1,0],[0, -1], [0, 1]]:
                    _r, _c = row + dr, col + dc
                    if (_r in range(rows) and 
                        _c in range(cols) and
                        grid[_r][_c] == "1" and
                        (_r, _c) not in visited):
                        queue.append((_r, _c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands

