"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cpy_map = dict()
        cpy_map[node] = Node(node.val)

        visited = set()
        q = deque()
        q.append(node)
        visited.add(node)

        while q:
            n = q.popleft()
            for nbr in n.neighbors:
                if nbr not in cpy_map:
                    cpy_map[nbr] = Node(nbr.val)
                cpy_map[n].neighbors.append(cpy_map[nbr])
                if nbr in visited:
                    continue
                q.append(nbr)
                visited.add(nbr)
        
        return cpy_map[node]