# Definition for a binary tree node.
import ast
class TreeNode(object):
    def __init__(self, x, left=None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root:
            return "[ " + str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right) + "," + "]"
        else:
            return "[]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        treelist = ast.literal_eval(data)
        return self.deserialize_helper(treelist)

    def deserialize_helper(self, treelist):
        if len(treelist) == 0:
            return None
        else:
            root = TreeNode(treelist[0])
            root.left = self.deserialize_helper(treelist[1])
            root.right = self.deserialize_helper(treelist[2])
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

'''
                        100
                    /        \
                  50             150      
                /    \         /     \
             30       70      130       180
           /   \     /  \     /  \      /   \
         10     31  60  71   95   135  170   190
'''

f1 = TreeNode(30, TreeNode(10), TreeNode(31))
f2 = TreeNode(70, TreeNode(60), TreeNode(71))
f3 = TreeNode(50, f1, f2)
f4 = TreeNode(130, TreeNode(101), TreeNode(135))
f5 = TreeNode(180, TreeNode(155), TreeNode(190))
f6 = TreeNode(150, f4, f5)
f7 = TreeNode(100, f3, f6)

def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)        
        printTree(root.right)


printTree(f7)
c = Codec()
s = c.serialize(f7)
print("serialized = ", s)
t = c.deserialize(s)
printTree(t)

