# leetcode: https://leetcode.com/problems/subarray-sum-equals-k
# two key ideas: sum(i+1:j) = sum(0:j) - sum(0:i)
# In order to take care of all possible ways of getting a 0 in an example such as [0,0,0,0,0] with k = 0
# we need to keep track of prefixes.
# d[v] = x implies that there are x prefixes with value v
# in the for loop, when we do count += d.get(p-k, 0), we are are adding the prefix count for value p-k.
# everytime you encounter the same sum p, d[p] goes up by 1, indicating that number of prefix sums
# that add up to p went up by 1
# 
# example: [0,0,0,1,0,0,0], k = 0
# iteration i = 0: count = 0; d.get(0-0, 0) = 1, count = 1, d[0] = 2
# iteration i = 1: count = 1; d.get(0-0, 0) = 2, count = 3, d[0] = 3
# iteration i = 2: count = 3; d.get(0-0, 0) = 3, count = 6, d[0] = 4
# iteration i = 3: count = 6; d.get(1-0, 0) = 0, count = 6, d[1] = 1
# iteration i = 4: count = 6; d.get(1-0, 0) = 1, count = 7, d[1] = 2
# iteration i = 5: count = 7; d.get(1-0, 0) = 2, count = 9, d[1] = 3
# iteration i = 6: count = 9; d.get(1-0, 0) = 3, count = 12, d[1] = 4

def subarraySum(nums, k):
    n = len(nums)
    p = 0
    d = {}
    count = 0
    d[0] = 1
    for i in range(n):
        p += nums[i]
        count += d.get(p - k, 0)
        d[p] = d.get(p, 0) + 1

    return count
