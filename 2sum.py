# https://leetcode.com/problems/two-sum/
# 
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index = 0
    d = {}
    for index in range(len(nums)):
        f = nums[index]
        j = target - f
        try:
            return [d[j], index]
        except KeyError:
            d[f] = index


print(twoSum([-1,0,1,2,-1,-4], 0))



