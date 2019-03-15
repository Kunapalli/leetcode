def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return helper(nums, 0)


def helper(nums, index):
    if len(nums) == 0 or index == len(nums):
        return [[]]
    else:
        s = helper(nums, index + 1)
        r = [x + [nums[index]] for x in s]
        return s + r


L = subsets([1,2,3,4])
print(len(L), L)


