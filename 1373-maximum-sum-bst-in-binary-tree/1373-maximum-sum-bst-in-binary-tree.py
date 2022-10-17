# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxS = 0
        def maxSum(root):
            nonlocal maxS
            l_valid, l_min, l_max, l_sum = maxSum(root.left) if root.left else [True, root.val, 0, 0]
            r_valid, r_min, r_max, r_sum = maxSum(root.right) if root.right else [True, 0, root.val, 0]
            
            root_valid = True 
            if root.left:
                root_valid &= root.val > l_max
            if root.right:
                root_valid &= root.val < r_min
            
            if l_valid and r_valid and root_valid:
                Sum = root.val + l_sum + r_sum
                maxS = max(maxS, Sum)
                return [True, l_min, r_max, Sum]
            return [False, l_min, r_max, max(l_sum, r_sum)]
            
        maxSum(root)
        return maxS