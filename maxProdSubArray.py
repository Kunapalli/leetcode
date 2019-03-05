# https://leetcode.com/problems/maximum-product-subarray/
# Runtime: 40 ms, faster than 100.00% of Python3 online submissions
# for Maximum Product Subarray.
# Memory Usage: 6.6 MB, less than 90.65% of Python3 online submissions
# for Maximum Product Subarray.

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    ## main algo

    n = len(nums)
    # curMax contains the max of a product of subarray that includes this number
    # curMin contains the min of a product of subarray that includes this number
    # example: [2, -5, 0, -2, -4, 3]
    # consider when we are procesing -4.
    # the max product that ends in -4 is -2*-4 = 8
    # min product that ends in -4 is just -4
    # example: [-1, -3, 4, 4, -1, 2, 1, -5, 4]
    # consider when processing -5.
    # max product that ends in -5 is product of -1*-3*4*4*-1*2*1*-5 = 480
    # min product that ends in -5 is product of -3*4*4*-1*2*1*-5 = -480
    
    curMax = curMin = prevMax = nums[0]
    i = 1
    while i < n:
        if nums[i] < 0:
            t = curMax
            curMax = curMin
            curMin = t
            
        curMax = max(nums[i], curMax*nums[i]) # by taking max of either nums[i] or product, zero is handled
        curMin = min(nums[i], curMin*nums[i])
        i += 1
        prevMax = max(prevMax, curMax)

    return prevMax



#print(maxProduct([0, 2, 3, -1, 3, 2, 3]))
#print(maxProduct([-2, 0, -1]))  # 0
#print(maxProduct([1, 0, 0, 0]))  # 1
#print(maxProduct([-2, 3, -4]))  # 24
#print(maxProduct([-1, -3, 4, 4, -1, 2, 1, -5, 4]))  # 1920
#print(maxProduct([3, 4, 5]))  # 60
#print(maxProduct([2, -5, 0, -2, -4, 3]))  # 24
#print(maxProduct([2, -5, 1, 1, 1]))  # 2
#print(maxProduct([-2, 1, 0]))  # 1
#print(maxProduct([0, 2]))  # 2
#print(maxProduct([-2]))  # -2
#print(maxProduct([2, 3, -2, 4]))  # 6
#print(maxProduct([0, 1, 2]))  # 2
#print(maxProduct([1, -1, 2]))  # 2
#print(maxProduct([-3, -2, -1]))  # 6
#print(maxProduct([-1, 2, 3, -20]))  # 120
#print(maxProduct([-1, 2, 3, -20, 0, 200]))  # 200
#print(maxProduct([-1, 1, -3, 4, 5]))  # 60
#print(maxProduct([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 960
#print(maxProduct([4, -3, -1, 4, -1, 2, 1, -5, 4]))  # 1920
#print(maxProduct([-1, -3, 4, 4, -1, 2, 1, -5, 4]))  # 1920
#print(maxProduct([1, 1, -2]))  # 1
