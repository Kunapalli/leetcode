# https://leetcode.com/problems/sort-colors/
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

# better approach (this is the dutch national flag problem posed by Dijkstra)

def sortColors(nums):
    n = len(nums)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if nums[mid] == 2:
            nums[mid] = nums[high]
            nums[high] = 2
            high -= 1
        elif nums[mid] == 0:
            nums[mid] = nums[low]
            nums[low] = 0
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
    print(nums)


sortColors([2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 1, 1, 2, 2, 0, 0, 0, 1])
sortColors([2, 2, 2])
sortColors([1,1,1])
sortColors([0,0,0])
sortColors([0,1,0,1,0,2,1,0,1,0,1,2])
