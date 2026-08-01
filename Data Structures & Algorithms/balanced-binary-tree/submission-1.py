# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return True, 0

            l_bal, l_ht = helper(node.left)
            r_bal, r_ht = helper(node.right)

            height = max(l_ht, r_ht) + 1

            if not l_bal or not r_bal:
                return False, height

            return abs(l_ht - r_ht) <= 1, height

        balanced, _ = helper(root) 

        return balanced

            