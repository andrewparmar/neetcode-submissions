class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {k:[] for k in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
            
            for nbr in adj[node]:
                if nbr != prev:
                    if not dfs(nbr, node):
                        return False
            
            return True

        return dfs(0, None) and len(seen) == n