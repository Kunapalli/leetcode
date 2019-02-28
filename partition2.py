# https://leetcode.com/problems/partition-equal-subset-sum/
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two
# subsets such that the sum of elements in both subsets is equal.
#
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.

# Key idea: Our sum has to be even. Then we assign half the sum to S.
# dp[k] = True implies that we can make a sum of k using the numbers in the array nums.
# Note the range in the second for loop. It is descending. Why?
# example: [1,5,11,5], S = 11
# we iterate over all nums in outer for
# we iterate from S to the number chosen in outer for
# in inner for, we always start with our goal of finding dp[S].
# In order to make j, given that we have nums[i], we just need to make sure we can make j - nums[i].
# Let us see what happens if the inner for loop was ascending: for j in range(nums[i], S+1, 1)
# when i = 0, j = 1, dp[1] = dp[0] = 1
# when i = 0, j = 2, dp[2] = dp[1] = 1 --> this is the problem. We have only one 1 but the algo thinks we can use as many
# ones as we like. There is no we way we can make 2 with the numbers we have. 

def partition(nums):
    """
    :type rods: List[int]
    :rtype: int
    """
    S = int(sum(nums))
    if S%2 == 1:
        return False

    S = S//2
    print(S)
    nums.sort()
    dp = [False]*(S+1)
    dp[0] = True
    for i in range(len(nums)):
        for j in range(S, nums[i]-1, -1):
            if not dp[j]:
                dp[j] = dp[j - nums[i]]

    return dp[S]


