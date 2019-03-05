# https://leetcode.com/problems/queue-reconstruction-by-height/
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of
# integers (h, k), where h is the height of the person and k is the number of people in front of this person
# who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
#Note:
#The number of people is less than 1,100.
#
#
#First we sort the list by descending order of first element and if equal, by 
# ascending order of second element
# The claim is this. When we add an element from this sorted list to L2, the index of
# the element is correctly positioned at the time of add. Why? For (h,k), inserting at
# k implies there are k elements before whose height is greater or equal. Because of
# the original sorting, we know all elements before this element have a height greater
# or equal to its height. So just inserting at correct index would work fine.
# [Note, this can move later but will preserve correctness. ]

def height(L1):
    L1.sort(key=lambda elem: (elem[0]*-1, elem[1]))
    print(L1)
    L2 = []
    for i in L1:
        L2.insert(i[1], i)

    print(L2)

    
height([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
