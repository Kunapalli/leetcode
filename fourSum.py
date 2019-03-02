# https://leetcode.com/problems/4sum/
#Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# This seems simple. Two for loops, for each of i,j find if the remaining have a two sum.
# The key thing from optimization perspective are the early termination cases.
# list is sorted. Suppose l and r are the left and right ends of the array
# So when we are looking sum of four elements, we know 4*nums[l] <= target <= 4*nums[r]
# So when we are looking sum of four elements, we know 3*nums[l] <= target <= 3*nums[r]
# So when we are looking sum of four elements, we know 2*nums[l] <= target <= 2*nums[r]
# These checks cut down on the processing in a huge way
#
def fourSum(nums, target):
    n = len(nums)
    if n <= 3:
        return []

    nums.sort()
    i = 0
    L = []
    store = {}
    
    while i < n:
        if target < 4*nums[i] or target > 4*nums[n-1]:
            break
        
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        j = i+1
        while j < n:
            target3 = target - nums[i]
            if target3 < 3*nums[j] or target3 > 3*nums[n-1]:
                break
            if j > i+1 and nums[j] == nums[j-1]:
                j += 1
                continue
            
            twoSum(nums[j+1:], nums[i], nums[j], target - nums[i] - nums[j], L, store)
            j += 1
        i += 1

    return L


def twoSum(nums, a, b, target, L, store):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    if n < 2:
        return
    else:
        left = 0
        right = n-1
        while left < right:
            if target < 2*nums[left] or target > 2*nums[right]:
                return
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                L.append([a, b, nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1


print(fourSum([-3,0,7,-2,-6,-5,1,5,-1,-8,-9,-8,7,1,1,3,1,10], 0))
#print(fourSum([5,5,3,5,1,-5,1,-2],4))
#print(fourSum([-1,2,2,-5,0,-1,4], 3))
#c = [-3,0,7,-2,-6,-5,1,5,-1,-8,-9,-8,7,1,1,3,1,10]
#c.sort()
#print(c)
#l = fourSum([-3,0,7,-2,-6,-5,1,5,-1,-8,-9,-8,7,1,1,3,1,10],0)
#print(len(l), l)

#print(threeSum([1, -2, -5, -4, -3, 3, 3, 5], 10))
#print(threeSum([-1,0,1,2,-1,-4]))
#print(threeSum([1,2,3,4]))
#print(threeSum([1,2,3,1, 2, 3, 4,5,-1, 0, -2, -3]))

#print(fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
#print(fourSum([5,5,3,5,1,-5,1,-2], 4))
#print(fourSum([1, 2, -2, -1], 0))
#print(fourSum([0, 0, 0, 0], 0))
#print(fourSum([-3, -2, -1, -1, 0, 1, 1, 2, 3], 0))
#print(fourSum([-1, -1, 0, 1, 1, 2, 3], 0))

