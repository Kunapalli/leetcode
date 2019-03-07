# https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.

    
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def printTree(root):
    if root:
        printTree(root.left)
        print(root.val)
        printTree(root.right)


def printFlatTree(root):
    if root:
        if root.left is not None:
            print("ERROR")
        print(root.val)
        printTree(root.right)


def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return root

    if not root.left and not root.right:
        return

    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
            
        if not stack:
            return
        
        node = stack.pop()
        root = node.right
        if node.left:
            node.right = node.left
            node.left = None
            while node and node.right:
                node = node.right
                node.left = None
            node.right = root
    return


'''
                        100
                    /        \
                  50             150      
                /    \         /     \
             30       70      130       180
           /   \     /  \     /  \      /   \
         10     31  60  71   95   135  170   190
'''

f1 = TreeNode(30, TreeNode(31), None)
f2 = TreeNode(70, None, TreeNode(71))
f3 = TreeNode(50, f1, f2)
f4 = TreeNode(130, TreeNode(101), TreeNode(135))
f5 = TreeNode(180, TreeNode(155), TreeNode(190))
f6 = TreeNode(150, f4, f5)
f7 = TreeNode(100, f3, f6)


flatten(f7)
printFlatTree(f7)
