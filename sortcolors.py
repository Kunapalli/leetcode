# https://leetcode.com/problems/sort-colors/
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

# First attempt - pretty lame

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zerocount = 0
    i = 0
    while i < n:
        x = nums[i]
        if nums[i] == 1:
                del nums[i]
                nums.insert(zerocount, 1)

        elif nums[i] == 0:
            zerocount += 1
            del nums[i]
            nums.insert(0, 0)

        i += 1
        


sortColors([2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 1, 1, 2, 2, 0, 0, 0, 1])
sortColors([2, 2, 2])
sortColors([1,1,1])
sortColors([0,0,0])
sortColors([0,1,0,1,0,2,1,0,1,0,1,2])
