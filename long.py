# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# implement Manacher's algorithm. Best explanation is https://www.youtube.com/watch?v=V-sEwsca1ak
# 
def preProcess(s):
    n = len(s)
    if n == 0:
        return "^$"
    t = "^"
    i = 0
    while i < n:
        t += '#' + s[i]
        i += 1

    t += '#$'
    return t


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    t = preProcess(s)
    print(t)
    n = len(t)
    P = [0]*n
    i = 1

    maxPalCenterID = 1
    C = R = 0

    while i < n-1:
        x = t[i]
        ii = 2*C - i

        if R > i:
            P[i] = min(R - i, P[ii])
        else:
            P[i] = 0

        while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
            P[i] += 1

        if P[i] > P[maxPalCenterID]:
            maxPalCenterID = i

        if i + P[i] > R:
            C = i
            R = i + P[i]

        i += 1

    maxPalSize = P[maxPalCenterID]
    palStartID = (maxPalCenterID - 1 - maxPalSize) // 2

    return s[palStartID:palStartID+maxPalSize]

