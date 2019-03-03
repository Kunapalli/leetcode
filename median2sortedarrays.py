## Runtime: 88 ms, faster than 91.71% of Python3 online submissions for Median of Two Sorted Arrays.

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    p = (m+n+1)//2 # p will be the middle element if odd; p will be the first of the two middle elements if even
    even = False

    if (m+n)%2 == 0:
        even = True
    i = 0
    j = 0
    count = 0
    prev = cur = 0
    while count <= p:
        prev = cur
        try:
            if nums1[i] < nums2[j]:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
                
            count += 1
        except IndexError:
            if i < m: 
                if even:
                    if count == p: # the two middle are from different arrays
                        return (prev + nums1[i])/2
                    else: # both middle are from nums1
                        return (nums1[i + p - count - 1] + nums1[i + p - count])/2
                else:
                    if count == p: # odd and middle was the last element processed
                        return prev
                    else: # odd and middle is somewhere in nums1
                        return nums1[i + p - count - 1] 
            elif j < n: 
                if even:
                    if count == p: # the two middle are from different arrays
                        return (prev + nums2[j])/2
                    else: # both middle are from nums2
                        return (nums2[j + p - count - 1] + nums2[j + p - count])/2
                else:
                    if count == p: # odd and middle was the last element processed
                        return prev
                    else: # odd and middle is somewhere in nums2
                        return nums2[j + p - count - 1]

    if count == 0:
        return None

    return (prev + cur)/2 if even else prev
        
        

x = findMedianSortedArrays([1, 3, 4], [2])
if x != 2.5:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([4], [1, 2, 3, 5])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([1, 2, 10], [4, 5, 6, 7, 8])
if x != 5.5:
    print("test failed: expected 5.5: got ", x)
else:
    print("test passed: expected 5.5: got ", x)


x = findMedianSortedArrays([1, 2, 8], [4, 5, 9, 10, 11])
if x != 6.5:
    print("test failed: expected 6.5: got ", x)
else:
    print("test passed: expected 6.5: got ", x)


x = findMedianSortedArrays([1, 2, 3, 5], [4])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([2], [1, 3])
if x != 2:
    print("test failed: expected 2: got ", x)
else:
    print("test passed: expected 2: got ", x)


x = findMedianSortedArrays([1, 3], [2])
if x != 2:
    print("test failed: expected 2: got ", x)
else:
    print("test passed: expected 2: got ", x)


x = findMedianSortedArrays([2], [1, 3, 4])
if x != 2.5:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([1, 2, 3], [4, 5, 6])
if x != 3.50:
    print("test failed: expected 3.5: got ", x)
else:
    print("test passed: expected 3.5: got ", x)

x = findMedianSortedArrays([1, 2], [3, 4, 5])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([1, 2, 3], [4, 5])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([1, 2, 3], [4])
if x != 2.50:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([1, 2, 3], [])
if x != 2:
    print("test failed: expected 2: got ", x)
else:
    print("test passed: expected 2: got ", x)

x = findMedianSortedArrays([], [4, 5, 6])
if x != 5:
    print("test failed: expected 5: got ", x)
else:
    print("test passed: expected 5: got ", x)

x = findMedianSortedArrays([1, 2, 3, 4], [])
if x != 2.50:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([], [4, 5, 6, 7])
if x != 5.50:
    print("test failed: expected 5.5: got ", x)
else:
    print("test passed: expected 5.5: got ", x)

x = findMedianSortedArrays([1,2], [1,2])
if x != 1.50:
    print("test failed: expected 1.5: got ", x)
else:
    print("test passed: expected 1.5: got ", x)

x = findMedianSortedArrays([4, 5, 6], [1, 2, 3])
if x != 3.50:
    print("test failed: expected 3.5: got ", x)
else:
    print("test passed: expected 3.5: got ", x)

x = findMedianSortedArrays([3, 4, 5], [1, 2])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([4, 5], [1, 2, 3])
if x != 3:
    print("test failed: expected 3: got ", x)
else:
    print("test passed: expected 3: got ", x)

x = findMedianSortedArrays([4], [1, 2, 3])
if x != 2.50:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([], [1, 2, 3])
if x != 2:
    print("test failed: expected 2: got ", x)
else:
    print("test passed: expected 2: got ", x)

x = findMedianSortedArrays([4, 5, 6], [])
if x != 5:
    print("test failed: expected 5: got ", x)
else:
    print("test passed: expected 5: got ", x)

x = findMedianSortedArrays([], [1, 2, 3, 4])
if x != 2.50:
    print("test failed: expected 2.5: got ", x)
else:
    print("test passed: expected 2.5: got ", x)

x = findMedianSortedArrays([4, 5, 6, 7], [])
if x != 5.50:
    print("test failed: expected 5.5: got ", x)
else:
    print("test passed: expected 5.5: got ", x)

x = findMedianSortedArrays([1,2], [1,2])
if x != 1.50:
    print("test failed: expected 1.5: got ", x)
else:
    print("test passed: expected 1.5: got ", x)
