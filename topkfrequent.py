import collections

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    d = collections.defaultdict(int)
    for i in nums:
        d[i] += 1

    l = [(key,value) for key,value in d.items()] # using k,v changes the value of k :-)
    l.sort(key = lambda e: e[1], reverse = True)
    L = [0]*k
    for i in range(k):
        L[i] = l[i][0]

    return L

print(topKFrequent([1,1,1,2,2,3], 2))

