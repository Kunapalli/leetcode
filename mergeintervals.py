# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals = sorted(intervals, key=lambda element: element.start)
    L = []
    i = 0
    n = len(intervals)
    if n == 1:
        return intervals
    for i in intervals:
        if L and i.start <= L[-1].end:
            L[-1].end = max(L[-1].end, i.end)
        else:
            L += [i]
    return L

def printIntervals(intervals):
    print([(x.start, x.end) for x in intervals])

def makeIntervals(l):
    L = []
    for i in l:
        L.append(Interval(i[0], i[1]))

    return L

printIntervals(merge(makeIntervals([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])))
printIntervals(merge([Interval(1,10), Interval(4,12), Interval(3, 15), Interval(3, 8)]))

printIntervals(merge([Interval(1,10), Interval(12,14)]))
printIntervals(merge([Interval(1,2), Interval(2,3), Interval(3,4)]))




