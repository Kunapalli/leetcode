# The count is the catalan numbers. 
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    L = []
    helper(0, 0, n, L, "")
    print(len(L))
    return L


def helper(left, right, n, L, curString):
    if left == n:
        L.append(curString + ")"*(n-right))
    else:
        helper(left + 1, right, n, L, curString +"(")
        if left > right:
            helper(left, right+1, n, L, curString +")")

for i in range(20):
    generateParenthesis(i)

