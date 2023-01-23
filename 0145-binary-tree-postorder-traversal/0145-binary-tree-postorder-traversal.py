# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(root, res):
            if root:
                post_order(root.left, res)
                post_order(root.right, res)
                res.append(root.val)
            return res
        return post_order(root, [])
