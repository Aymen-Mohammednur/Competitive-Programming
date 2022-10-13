# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSuccessor(node):
            node = node.right
            while node.left:
                node = node.left
            return node
        def findPredecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node
        
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.right:
                succ = findSuccessor(root)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
            else:
                pre = findPredecessor(root)
                root.val = pre.val
                root.left = self.deleteNode(root.left, pre.val)
                
        return root