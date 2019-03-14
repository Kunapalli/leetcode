def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    output = [1]*(n)

    # in first pass output[i] will include product of all numbers with index >=i
    output[n-1] = nums[n-1]
    for i in range(n-2, 0, -1):
        output[i] = nums[i]*output[i+1]

    # in second pass, keep a product of all numbers in front and multiply by what we have stored in output so far
    x = 1
    for i in range(0, n-1, 1):
        output[i] = x * output[i+1]
        x *= nums[i]
        
    output[i+1] = x
    return output

print(productExceptSelf([1,2,3,4,5,6,7,8,9,10,11]))

