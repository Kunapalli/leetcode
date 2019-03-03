# Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 7.1 MB, less than 83.92% of Python3 online submissions for Maximum Subarray.


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return None

    prevMax = curMax = nums[0]
    i = 1

    # at any point, you are making curMax better or worse by adding nums[i]. Choose the highest
    # compare with prevMax and store the highest as prevMax
    while i < n:
        curMax = max(nums[i], curMax + nums[i])  
        prevMax = max(prevMax, curMax)
        i += 1

    return prevMax


print(maxSubArray([-1, 0, -2]))  # 3
print(maxSubArray([0, 1, 2]))  # 3
print(maxSubArray([1, -1, 2]))  # 2
print(maxSubArray([-3, -2, -1]))  # -1
print(maxSubArray([-1, -2, -3]))  # -1
print(maxSubArray([-1, 1, -3, 4, 5]))  # 9
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSubArray([4, -3, -1, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSubArray([-1, -3, 4, 4, -1, 2, 1, -5, 4]))  # 10
print(maxSubArray([1, 1, -2]))  # 2
