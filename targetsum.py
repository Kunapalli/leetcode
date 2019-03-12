# https://leetcode.com/problems/target-sum/

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each
# integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Algorithm:
# in front of each n numbers we can have either + or -. So total possibilities are 2^n,
# How do we cut this down? Idea. Divide the list ansd compute all possible numbers and store them in dict.
# Since we know list is at most 20, each sub list is only 10 and we will have 1024 values.
# then we do dict lookup

import time
import collections


def findTargetSumWays(nums, S):
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return 1 if S == nums[0] or S == -nums[0] else 0

    d1 = collections.defaultdict(int)
    d2 = collections.defaultdict(int)

    # divide the list into two more or less equal lists
    n1 = nums[0:n//2]
    n2 = nums[n//2:]

    # initialize d1 with the first number (both positive and negative value)
    d1[n1[0]] += 1
    d1[-n1[0]] += 1

    # for each number left, we add and subtract from every key in d1.
    for j in n1[1:]:
        cur = collections.defaultdict(int)
        for k in d1:
            cur[k+j] += d1[k]
            cur[k-j] += d1[k]
        d1 = cur

    # initialize d2 with the first number (both positive and negative value)        
    d2[n2[0]] += 1
    d2[-n2[0]] += 1    

    # for each number left, we add and subtract from every key in d2
    for j in n2[1:]:
        cur = collections.defaultdict(int)        
        for k in d2:
            cur[k+j] += d2[k]
            cur[k-j] += d2[k]
        d2 = cur

    # for each key 'k' in d1, we check if 'S - k' is in d2. If so we multiply the values.
    count = 0
    for k in d1:
        if S - k in d2:
            count += d1[k] * d2[S-k]

    return count


t0 = time.time()
print(findTargetSumWays([1,1,1,1,1], 3))
print(findTargetSumWays([22,36,7,44,38,32,16,32,1,16,25,45,49,45,27,9,41,31,10,15], 1))
print(findTargetSumWays([6,20,22,38,11,15,22,30,0,17, 34,29,7,42,46,49,30,7,14,5], 28))
print(findTargetSumWays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19,19], 1))
print(time.time() - t0)

