# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# use mergeSort to merge two lists at a time until there is only one list

def mergeKLists(lists):
    
    n = len(lists)

    if n == 0:
        return []
    elif n == 1:
        return lists[0]
    else:
        while len(lists) > 1:
            L = []
            j = 0
            n = len(lists)
            while j < n: # if we start with n = 2^m lists, we will do 2^(m-1) mergesorts in each iteration
                L.append(mergeSort(lists[j], lists[j+1])) 
                if j + 3 == n:
                    L.append(lists[j+2])
                    break
                else:
                    j += 2
            lists = L
    
        return lists[0]


def mergeSort(l1, l2):
    h = p = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    if not l1:
        p.next = l2
    elif not l2:
        p.next = l1

    return h.next


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

def lenList(l):
    i = 0
    k = l
    while k:
        i += 1
        k = k.next
    return i


def printList(L):
    while L:
        print(L.val)
        L = L.next


#print(mergeSort([1, 2, 3], [1, 2, 3]))
#print(mergeSort([4, 5, 6], [1, 2, 3]))
#print(mergeSort([1, 2, 4], [-1, 3, 4]))

printList(mergeKLists([makeList([1,2,3]), makeList([-1,3,4,9,8,7]),
                       makeList([4,5]), makeList([-100, 0, 100, 1000, 1, 0])]))


