# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path(node, max_sum):
            if not node:
                return 0
            left_sum = max(max_path(node.left, max_sum), 0)
            right_sum = max(max_path(node.right, max_sum), 0)
            path_sum = node.val + left_sum + right_sum
            
            max_sum[0] = max(max_sum[0], path_sum)
            
            return node.val + max(left_sum, right_sum)
        
        max_sum = [float('-inf')]
        max_path(root, max_sum)
        return max_sum[0]