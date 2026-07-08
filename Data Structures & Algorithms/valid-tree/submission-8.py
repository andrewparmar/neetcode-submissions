class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {x:[] for x in range(n)}

        for n1, n2 in edges:
            # if n1 == n2:
            #     return False
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)
        seen = set()

        def dfs(prev, node):
            # if prev == node:
            #     return False
            if node in seen:
                print("returning False", node)
                return False

            seen.add(node)

            for nbr in adj[node]:
                print("prev", prev, "node", node, "nbr", nbr)
                if nbr == prev:
                    continue
                if not dfs(node, nbr):
                    return False

            return True

        seen = set()
        if not dfs(None, 0):
            return False
        if not len(seen) == n:
            return False

        return True
        