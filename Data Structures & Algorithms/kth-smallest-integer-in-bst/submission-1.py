# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = None

        def dfs(node):
            nonlocal counter, res
            if not node:
                return

            dfs(node.left)
            counter += 1
            if counter == k:
                res = node
                return
            dfs(node.right)

        dfs(root)

        return res.val