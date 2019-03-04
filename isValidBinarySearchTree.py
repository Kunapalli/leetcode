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

def isValidBST(root: TreeNode):
    return isValidBSTHelper(root, float('-inf'), float('inf'))

        
def isValidBSTHelper(root: TreeNode, min_, max_):
    if root is None:
        return True

    # the root has to be > min_ and less than max_
    if root.val <= min_ or root.val >= max_:
        return False
    
    left = right = True
    if root.left:
        # consider root at 70. All children > 50 and < 70
        left = isValidBSTHelper(root.left, min_, min(root.val, max_)) 
    if root.right:
        # consider root at 135. All children > 100 and < 130
        right = isValidBSTHelper(root.right, max(root.val, min_), max_)

    return left and right
        
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
print(isValidBST(f1))
print(isValidBST(f2))
print(isValidBST(f3))
print(isValidBST(f4))
print(isValidBST(f5))
print(isValidBST(f6))
print(isValidBST(f7))
