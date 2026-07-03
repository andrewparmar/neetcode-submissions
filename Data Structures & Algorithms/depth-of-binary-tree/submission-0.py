# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        find maxDepth of left
        find maxDepth of right
        return max between the two + 1
        """
        # node 1, 
        if not root: 
            return 0

        left = self.maxDepth(root.left) # 1
        right = self.maxDepth(root.right) # 

        return max(left, right) + 1