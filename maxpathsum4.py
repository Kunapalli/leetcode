# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to
# any node in the tree along the parent-child connections. The path must contain at least one
# node and does not need to go through the root.

class TreeNode(object):
    def __init__(self, x, left=None, right = None):
        self.val = x
        self.left = left
        self.right = right

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return None
    curmax = [-float('inf')]
    _,_ = helper(root, curmax)
    return curmax[0]

def helper(root, curmax):
    if root is None:
        return None, False
    print("in helper: root is ", root.val)
    m = root.val
        
    (maxleft, vialeftroot) = helper(root.left, curmax)
    (maxright, viarightroot) = helper(root.right, curmax)
        
    if m < 0:
        if vialeftroot and viarightroot:
            m2 = max(maxleft, maxright, maxleft + maxright + m)
            curmax[0] = max(curmax[0], m2)
            if maxleft > maxright:
                return (maxleft + m, True) if maxleft + m > 0 else (None, False)
            else:
                return (maxright + m, True) if maxright + m > 0 else (None, False)
        
        elif vialeftroot:
            curmax[0] = max(curmax[0], maxleft)
            return (maxleft + m, True) if maxleft + m > 0 else (None, False)
        
        elif viarightroot:
            curmax[0] = max(curmax[0], maxright)
            return (maxright + m, True) if maxright + m > 0 else (None, False)
        
        else:
            curmax[0] = max(curmax[0], m)
            return None, False
        
    else:
        if vialeftroot and viarightroot:
            print("both: m = {}, maxleft {}, maxright {}".format(m, maxleft, maxright))
            curmax[0] = max(curmax[0], m + maxleft + maxright)
            print("1: curmax is ", curmax[0])
            return max(m + maxleft, m + maxright), True
        
        elif vialeftroot:
            print("vialeft: m = {}, maxleft {}".format(m, maxleft))
            curmax[0] = max(curmax[0], m + maxleft)
            print("2: curmax is ", curmax[0])
            return m + maxleft, True
        
        elif viarightroot:
            print("viaright: m = {}, maxright {}".format(m, maxright))            
            curmax[0] = max(curmax[0], m + maxright)
            print("3: curmax is ", curmax[0])
            return m + maxright, True
        
        else:
            print("vianone: m = {}".format(m)) 
            curmax[0] = max(curmax[0], m)
            print("4: curmax is ", curmax[0])                
            return m, True
        
        


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
f3 = TreeNode(-50, f1, f2)
f4 = TreeNode(-100, TreeNode(95), TreeNode(135))
f5 = TreeNode(-1, TreeNode(170), TreeNode(190))
f6 = TreeNode(1, f4, f5)
f7 = TreeNode(1, f3, f6)

def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)        
        printTree(root.right)

#f2 = TreeNode(-6, TreeNode(5), TreeNode(9))
#f1 = TreeNode(8, TreeNode(9), f2)
printTree(f7)
print("****")
print(maxPathSum(f7))
