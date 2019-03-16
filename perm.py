def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    L = []
    n = len(nums)
    i = 0
    while i < n:
        if not L:
            L.append([nums[i]])
        else:
            newl = []
            for elem in L:
                for j in range(0, i+1):
                    e = elem[:]
                    e.insert(j, nums[i])
                    newl.append(e)
            L = newl
        i += 1

    return L

print(permute([1,2,3,4,5]))


        
    
