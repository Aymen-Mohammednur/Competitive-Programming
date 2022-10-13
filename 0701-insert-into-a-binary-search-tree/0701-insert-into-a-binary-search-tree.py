# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        def insert(curr):
            if curr:
                if val > curr.val:
                    if curr.right:
                        return insert(curr.right)
                    else:
                        curr.right = TreeNode(val)
                        return
                else:
                    if curr.left:
                        return insert(curr.left)
                    else:
                        curr.left = TreeNode(val)
                        return
        insert(curr)
        return root