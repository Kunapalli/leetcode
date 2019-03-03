# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Add all nodes of all lists to a dictionary by keeping track of duplicates
#
def mergeKLists(lists):
    countDict = {}

    for li in lists:
        while li:
            b = li.next # need to store this due to python's reference eccentricties
            if li.val in countDict:
                a = li
                x = countDict[li.val]
                a.next = x
                countDict[li.val] = a
            else:
                a = li
                a.next = None
                countDict[a.val] = a
            li = b 

    if not countDict:
        return None

    head = None

    sortedbyvalue = sorted(countDict.items(), key=lambda kv: kv[0])
    for key, val in sortedbyvalue:
        if head is None:
            head = val
            tmp = head
            while tmp.next:
                tmp = tmp.next
        else:
            tmp.next = val
            tmp = tmp.next
            while tmp.next:
                tmp = tmp.next

    return head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makeList(L):
    i = 0
    M = None
    tmp = None
    while i < len(L):
        if M is None:
            tmp = ListNode(L[i])
            M = tmp
        else:
            tmp.next = ListNode(L[i])
            tmp = tmp.next
        i += 1
    return M


def printList(l):
    if not l:
        print("None")
    k = l
    while k:
        print(k.val)
        k = k.next


# L1 = makeList([4, 5, 6])
# L2 = makeList([1, 2, 3])
# printList(L1)
# printList(mergeSort(L1, L2))


#print(mergeSort([1, 2, 3], [1, 2, 3]))
#print(mergeSort([4, 5, 6], [1, 2, 3]))
#print(mergeSort([1, 2, 4], [-1, 3, 4]))

printList(mergeKLists([makeList([1, 2, 3]), makeList([-1, 3, 4, 7, 8, 9, ]),
                     makeList([4, 5]), makeList([-100, 0, 0, 1, 100, 1000])]))


printList(mergeKLists([makeList([1, 2, 2]),makeList([1, 1, 2])]))
printList(mergeKLists([makeList([]), makeList([])]))


