# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, node, minimum, maximum):
        if not node:
            return True
        if minimum < node.val < maximum:
            return self.helper(node.left, minimum, node.val) and self.helper(node.right, node.val, maximum)
        return False