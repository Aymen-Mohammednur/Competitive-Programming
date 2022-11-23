# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ',' + '$'
        return ',' + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:].split(',')
        if data[0] == '$':
            return
        self.i = 0
        def pre_order():
            if data[self.i] == '$':
                self.i += 1
                return None
            root = TreeNode(data[self.i])
            self.i += 1
            root.left = pre_order()
            root.right = pre_order()
            return root
        return pre_order()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))