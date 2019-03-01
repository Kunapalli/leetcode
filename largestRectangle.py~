'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the
area of largest rectangle in the histogram.
this is how the algo works
A rectangle will contribute in full in area calculations if subsequent rectangles are taller.
However, if a sequence of non-decreasing
rectangles is followed by a shorter rectangle, then we need to adjust.
Example: consider the heights 2,1,5,6,7,5,2
When we encounter 1, we cannot have a rectangle of height 2 stretch to right.
similarly the rectangle of height 5 ends when we see the last 2. 
As long as I keep seeing non decreasing values, add the index i to stack. 
if i see a value less than or equal to the previous value (as in cur <= heights[stack[-1]]). 
stack[-1] contains the last index added. and heights with that index gets the value of the last height
now while I find elements greater or equal to this height, keep popping stack and process the element. 
Note I do not process the current element in this stack loop (the inner loop)
For each element, I know its height and width. Width will be equal to i when 
stack is empty and if stack is empty we know the last element added was equal to the
very first element of the heights array and hence its width should be equal to i
if stack is not empty, then the distance between the current index i and last index in stack is i - stack[-1] - 1.
Why the -1? since we incremented i at the end of the stack loop
example: heights 2,1,5,6,7,5,2

----values at start of each iteration---   ------- values at end of each iteration ---
i  heights[i]  cur   stack       prevBestArea               stack     prevBestArea    
0    2          2      []             0                       [0]           0
1    1          1      [0]            0                       [1]           2
2    5          5      [1,2]          2                       [1,2]         2
3    6          6      [1,2,3]        2                       [1,2,3]       2
4    7          7      [1,2,3,4]      2                       [1,2,3,4]     2
5    5          5      [1,2,3,4]      2                       [1,5]         20
6    2          2      [1,5]          20                      [1,6]         20
7    n/a        -1     [1,6]          20                      []            20
'''

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    n = len(heights)
    
    prevBestArea = 0
    i = 0
    stack = []
    
    while i < n + 1:
        print("stack beg = {}, i = {}".format(stack, i))
        
        cur = -1 if i == n else heights[i]
        
        while stack and cur <= heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else (i - stack[-1] - 1)
            print("prev1 {}".format(prevBestArea))
            prevBestArea = max(prevBestArea, h*w)
            print("prev12 {}, h {}, w {}, stack = {}, i = {}".format(prevBestArea, h, w, stack, i)) 
        stack.append(i)
        i += 1
    return prevBestArea



print(largestRectangleArea([2,1,5,6,7,5,2]))
#print(largestRectangleArea([1,2,2,2]))
#print(largestRectangleArea([2,1,1,1]))

#print(largestRectangleArea([6, 0, 0, 1, 9, 4, 4, 0, 9, 1, 4]))  # 12
#print(largestRectangleArea([0, 2, 0]))  # 2
#print(largestRectangleArea([5, 3, 1, 0, 1]))  # 6
#print(largestRectangleArea([5, 1]))  # 5
#print(largestRectangleArea([1, 2, 3]))  # 4
#print(largestRectangleArea([2, 3, 4, 5, 3, 7, 8]))  # 18
#print(largestRectangleArea([2, 3, 4, 5, 2]))  # 10
#print(largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]))  # 20
#print(largestRectangleArea([1, 2, 1]))  # 3
#print(largestRectangleArea([1, 3, 5, 2]))  # 6
#print(largestRectangleArea([1, 2, 2]))  # 4
#print(largestRectangleArea([2, 3, 4]))  # 6
#print(largestRectangleArea([5, 3, 1]))  # 6
#print(largestRectangleArea([0, 0]))  # 0
#print(largestRectangleArea([0, 9]))  # 9
#print(largestRectangleArea([9, 0]))  # 9

