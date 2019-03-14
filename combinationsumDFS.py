# https://leetcode.com/problems/combination-sum/submissions/

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in
# candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# The DP solution is lot slower as we need to keep track of duplicates
def combinationSum(candidates, target):
    """
    :type rods: List[int]
    :rtype: int
    """
    candidates.sort()
    return helper(candidates, 0, target)


def helper(candidates, i, target):

    if target == 0:
        return [[]]
    
    res = []
    for i in range(i, len(candidates)):
        if target < candidates[i]:
            break
        
        res2 = helper(candidates, i, target - candidates[i])
        if res2:
            for j in res2:
                res.append(j + [candidates[i]])

    return res
    

print(combinationSum([2,3,5,7],21))
#m = partition([1, 2, 3, 4, 5, 6, 7, 8], 10)

