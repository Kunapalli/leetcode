# https://leetcode.com/problems/next-permutation/
# idea: start from the least significant digit and keep going until you find a number lower (call this index i-1)
# than its previous number (index i)
# Now we need to look for the smallest number (index k) greater than nums[i-1] and swap these two.
# next there is some basic bookkeeping.
# we know nums[0:i] are in right order. To this we need to attach sorted(nums[i:]) without losing the nums reference

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n <= 1:
        return
    
    i = n-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.sort()
    else:
        k = i
        while k < n and nums[k] > nums[i-1]:
            k += 1

        tmp = nums[i-1]
        nums[i-1] = nums[k-1]
        nums[k-1] = tmp
        L = sorted(nums[i:])
        del nums[i:]
        nums += L

        
#L = [7,9,8,8,8,0,5,0,5,4,1]
L = [7,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,2,6,6,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1]
print(L)
nextPermutation(L)
print(L)
#nextPermutation([2, 3, 1])

