def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    c = [0] * (n+1)
    c[0] = 1
    c[1] = 1
    for i in range(2, n+1, 1):
        for k in range(0,i):
            c[i] += c[k]*c[i-k-1]

    return c[n]


print(numTrees(3))

    
            
        
