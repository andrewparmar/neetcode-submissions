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

        old_2_new = dict()
        q = collections.deque()

        q.append(node)
        while q:
            curr = q.popleft()
            if curr not in old_2_new:
                old_2_new[curr] = Node(curr.val)
            cpy = old_2_new[curr]
            
            for nbr in curr.neighbors:
                if nbr not in old_2_new:
                    old_2_new[nbr] = Node(nbr.val)
                    q.append(nbr)
                nbr_cpy = old_2_new[nbr]
                cpy.neighbors.append(nbr_cpy)

        return old_2_new[node]