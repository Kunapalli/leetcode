# https://leetcode.com/problems/container-with-most-water/
# Runtime: 32 ms, faster than 99.28% of Python online submissions for Container With Most Water.
# Memory Usage: 11.6 MB, less than 1.41% of Python online submissions for Container With Most Water.
# the left and right edge are the boundaries. So we work our way in from left extreme and right extreme.
# Regardless of how tall intermediate heights are, the two ends can hold water proportional to the smaller height
# and the width given by right - left. 

def maxArea(heights):
    """
    Time:  O(n)
    Space: O(1)
    """
    max_area = 0
    
    left = 0
    right = len(heights) - 1
    
    while left < right:
        if heights[left] > heights[right]:
            area = heights[right]*(right - left)
            right -= 1
        else:
            area = heights[left]*(right - left)
            left += 1
                
        if max_area < area:
            max_area = area

    return max_area
