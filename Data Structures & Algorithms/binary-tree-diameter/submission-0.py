# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, max_diameter = self.helper(root)
        return max_diameter

    def helper(self, node):
        if not node:
            return 0, 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        depth = max(left[0], right[0]) + 1

        diameter = left[0] + right[0]

        max_diameter = max(left[1], right[1], diameter)

        return depth, max_diameter
        