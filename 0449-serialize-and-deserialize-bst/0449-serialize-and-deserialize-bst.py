# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ',' + '$'
        return ',' + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data[1:].split(',')
        if data[0] == '$':
            return
        self.i = 0
        return self.pre_order(data)
    
    def pre_order(self, data):
        if data[self.i] == '$':
            self.i += 1
            return None
        root = TreeNode(data[self.i])
        self.i += 1
        root.left = self.pre_order(data)
        root.right = self.pre_order(data)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans