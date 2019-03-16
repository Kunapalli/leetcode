import collections

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    L = []
    q = collections.deque()
    q.append(root)
    curList = []
    n = len(q)
    i = 0
    
    while i < n: 
        node = q.popleft()
        curList.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        i += 1

        if i == n: # end of a level, so append curList to L
            L.append(curList)
            curList = []
            n = len(q)
            i = 0
    return L

'''
                        100
                    /        \
                  50             150      
                /    \         /     \
             30       70      130       180
           /   \     /  \     /  \      /   \
         10     31  60  71  101   135  170   190
'''

f1 = TreeNode(30, TreeNode(10), TreeNode(31))
f2 = TreeNode(70, TreeNode(60), TreeNode(71))
f3 = TreeNode(50, f1, f2)
f4 = TreeNode(130, TreeNode(101), TreeNode(135))
f5 = TreeNode(180, TreeNode(155), TreeNode(190))
f6 = TreeNode(150, f4, f5)
f7 = TreeNode(100, f3, f6)

print(levelOrder(f7))
