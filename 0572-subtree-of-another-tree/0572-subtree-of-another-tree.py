# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root, val, order):
        order.append(val)
        if val != None:
            if root.left: self.preOrder(root.left, root.left.val, order)
            else: self.preOrder(root, None, order)
            
            if root.right: self.preOrder(root.right, root.right.val, order)
            else: self.preOrder(root, None, order)
        
        return order
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootOrder = self.preOrder(root, root.val, [])
        subOrder = self.preOrder(subRoot, subRoot.val, [])
        
        r, s = len(rootOrder), len(subOrder)
        for i in range(r - s + 1):
            if rootOrder[i : i+s] == subOrder: return True
        return False