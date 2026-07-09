class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {x:[] for x in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen = set()

        def dfs(prev, node):
            if node in seen:
                return False

            seen.add(node)
            for nbr in adj[node]:
                if nbr == prev:
                    continue
                if not dfs(node, nbr):
                    return False
            return True

        return dfs(None, 0) and len(seen) == n
        