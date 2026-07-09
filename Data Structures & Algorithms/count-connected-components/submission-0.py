class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        seen = set()
        adj = {k:[] for k in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(prev, node):
            if node in seen:
                return
            seen.add(node) 
            for nbr in adj[node]:
                if nbr == prev:
                    continue
                dfs(node, nbr)

        for k in adj.keys():
            if not k in seen:
                cc += 1
            dfs(None, k)

        return cc
