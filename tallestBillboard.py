# https://leetcode.com/problems/tallest-billboard/

# You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.
# Each steel support must be an equal height.

# You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you
# can weld them together to make a support of length 6.

# Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

import time
import collections
from collections import defaultdict


# why does this work? Take [1,2,3]
# let us start with brute force. Any element can be added left, right or not at all.
# When we process 1, (0,0) leads to (1,0), (0,1), (0,0) ; 1:1, 0:0, -1:0
# when we process 2: (1,0) leads to (3,0), (1,2), (1,0);  3:3, 1:1, -1:1
#                    (0,1) leads to (2,1), (0,3), (0,1)
#                    (0,0) leads to (2,0), (0,2), (0,0)
# Key observation is when the difference of the tuples is the same. For example (0,1) and (1,2) have a difference of -1.
# we can discard one of them. But why? let us continue:
#
# when we process 3:
#                  1. (3,0) leads to (6,0), (3,3), (3,0)
#                  2. (1,2) leads to (4,2), (1,5), (1,2)
#                  3. (1,0) leads to (4,0), (1,3), (1,0)
#                  4. (2,1) leads to (5,1), (2,4), (2,1)
#                  5. (0,3) leads to (3,3), (0,6), (0,3)
#                  6. (0,1) leads to (3,1), (0,4), (0,1)
#                  7. (2,0) leads to (5,0), (2,3), (2,0)
#                  8. (0,2) leads to (3,2), (0,5), (0,2)
#                  9. (0,0) leads to (3,0), (0,3), (0,0)
# now notice bullets 2 and 6. These started with (1,2) and (0,1) and
# continue to produce triples with the same difference.
# for example, (4,2) is 1 more than (3,1); (1,5) is 1 more than(0,4) and
# (1,2) is 1 more than (0,1). Since this will continue,
# we discard anything with the same difference but the largest sum
# all we are doing below is keep difference as key and sum of the left as the value.
# Nothing magical about this, We could instead keep the difference as key and
# sum of right also value as in tallestBillboard2 below


def tallestBillboard(rods):
    """
    :type rods: List[int]
    :rtype: int
    """
    store = {0: 0}
    for i in rods:
        cur = collections.defaultdict(int)
        for j in store:
            # Think of a balance where we add to the left or the right
            # We can add to the left, right or not use this rod
            # key = difference between left and right
            # value = sum of weight in left
            cur[j + i] = max(store[j] + i, cur[j+i]) # adding to left. New key is old key + i.
            cur[j] = max(store[j], cur[j]) # not using this rod. New key is old key.
            cur[j - i] = max(store[j], cur[j-i]) # adding to right. New key is old key - i.
            # some explanation for the value part. We can have left = 1 and right = 0 and have a key of 1 and vqlue of 1
            # or we can have left as 21, right as 20 with key of 1 and value of 21. In such cases, we prefer to store the max value
            # so that we dont duplicate sub-problems. Holding onto (1,1) is pointless as we will reach (21,20) again after some iterations.
            # This pruning is the optimization we do and cuts down heavily on computation
        store = cur
    return store[0]


def tallestBillboard2(rods):
    """
    :type rods: List[int]
    :rtype: int
    """
    store = {0: 0}
    for i in rods:
        cur = collections.defaultdict(int)
        for j in store:
            # case when we will add to right
            cur[j + i] = min(store[j], cur[j+i])
            cur[j] = min(store[j], cur[j])
            cur[j - i] = min(store[j] - i, cur[j-i])
        store = cur
    return store[0]


t0 = time.time()
m = tallestBillboard([1,2,3])
print("m is ",  m)
m = tallestBillboard([1, 2, 3, 4, 5, 6, 7, 8])
print("m is ",  m)
m = tallestBillboard([52, 61, 69, 53, 64, 69, 63, 78, 66, 65, 68, 78, 65, 68, 81, 800, 800, 800, 800, 800])
print("m is ",  m)
m = tallestBillboard([1, 2, 3, 4, 5, 6, 7, 8])
print("m is ",  m)
m = tallestBillboard([1,  2,  3,  4,  5,  6,  7,  8,  9,  10])
print("m is ",  m)
m = tallestBillboard([ 162,  161, 149, 180, 146, 149, 146, 148, 145, 134, 138, 138, 153, 151])
print("m is ",  m)
m = tallestBillboard([98, 90, 101, 90, 108, 112, 106, 87, 90, 117, 99, 89, 113, 100])
print("m is ",  m)
m = tallestBillboard([1, 2, 4, 8, 16, 32, 64, 128, 256, 512,  50, 50, 50, 150, 150, 150, 100, 100, 100, 123])
print("m is ",  m)
m = tallestBillboard([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
print("m is ",  m)
print(time.time() - t0)
