# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, float("-inf")

            l_ht_sum, l_max_path = helper(node.left)
            r_ht_sum, r_max_path = helper(node.right)

            root_sum =max(0, l_ht_sum) + node.val + max(0, r_ht_sum)

            max_path = max(root_sum, l_max_path, r_max_path)
            max_leg_sum = max(node.val + l_ht_sum, node.val + r_ht_sum, node.val)

            return max_leg_sum, max_path

        return max(helper(root))
        