# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
#Note:
#
#The solution set must not contain duplicate triplets.
# Why cant we just use 2sum to solve this? because the target is 0, at least one of the numbers must be
# negative.
# first sort the list of numbers
# -3 -3 -2 -1 0 1 2 3
# We start with i = 0.
# first, we stop if we see a positive number as three positive numbers cannot equal 0
# second, Then we keep two indices left and right. Left starts with i+1 (first element after i)
# and right starts with n-1 (the last element). If the first element is 0, then other two are zero.
# if first element < 0, then one of the other two elements must be > 0. 
# Third, if current element is same as previous element, then no need to process this as we would have
# done so in the previous iteration/ 
# Inner while loop:
# we stop when left and right meet 
# we check to see if nums[i] + nums[left] + nums[right] is <, = or > 0
# if < 0, then we need to move right (since list is sorted, subsequent numbers are >= current element)
# if < 0, then we need to move left (since list is sorted, subsequent numbers are <= current element)
# if = 0, we store this triple.
# and as long as subsequent elements to the right are the same as nums[left], increment left
# and as long as subsequent elements to the left are the same as nums[right], decrement right

def threeSum(nums):
    
    n = len(nums)
    if n <= 2:
        return []

    i = 0
    nums.sort()
    L = []
    while i < n-2:
        right = n-1
        left = i+1
        if nums[i] > 0: 
            break

        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
            continue

        while left < right:
            a = nums[i]
            b = nums[left]
            c = nums[right]
            sum = a + b + c
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                L.append([a, b, c])

                # not worth trying to optimize these two whiles in a single while :-)
                while left < right and nums[left] == nums[left+1]:
                        left += 1
                while left < right and nums[right] == nums[right-1]:
                        right -= 1
                left += 1
                right -= 1
        i += 1


    return L


print(threeSum([-3, -3, 6]))
#print(threeSum([1,2,-2,-1]))

#print(threeSum([0, 0, 0, 0]))

#print(threeSum([-3, -2, -1, -1, 0, 1, 1, 2, 3]))

#print(threeSum([-1,0,1,2,-1,-4]))

#print(threeSum([1,2,3,4]))

#print(threeSum([1,2,3,1, 2, 3, 4,5,-1, 0, -2, -3]))
