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

            if not l_bal or not r_bal:
                return False, max(l_ht, r_ht) + 1

            return abs(l_ht - r_ht) <= 1, max(l_ht, r_ht) + 1

        balanced, _ = helper(root) 

        return balanced

            