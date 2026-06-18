class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj_list = {i:[] for i in range(n)}
        for (a, b) in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        
        def dfs(node, visited, prev):
            if node in visited:
                return False
            visited.add(node)

            for nbr in adj_list[node]:
                if nbr != prev and not dfs(nbr, visited, node):
                    return False
            return True
        
        return dfs(0, visited, -1) and len(visited) == n
