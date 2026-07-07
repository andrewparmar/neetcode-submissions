from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visited_pac = set()
        visited_atl = set()

        def bfs(cell, visited):
            if cell in visited:
                return
            
            q = deque()
            q.append(cell)
            visited.add(cell)

            while q:
                row, col = q.popleft()
                for dr, dc in [-1,0],[1,0],[0,-1],[0,1]:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        (r, c) not in visited and
                        heights[row][col] <= heights[r][c]):
                        q.append((r,c))
                        visited.add((r,c))

        for c in range(cols):
            bfs((0, c), visited_pac)
            bfs((rows-1, c), visited_atl)

        for r in range(rows):
            bfs((r, 0), visited_pac)
            bfs((r, cols-1), visited_atl)

        return list(visited_pac.intersection(visited_atl))
        


