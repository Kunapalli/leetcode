# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# implement Manacher's algorithm. Best explanation is https://www.youtube.com/watch?v=V-sEwsca1ak
# this is not my code but I don't see any need to change this beautiful code.
# 
# consider string afabcabaabcde
# after processing, string becomes ^#a#f#a#b#c#a#b#a#a#b#c#d#e#$
#
'''
------------beginning of each iteration---------------    ------at end of iteration ----
i    t[i]    C       R      ii    maxPalCenterID   P[i]   P[i] maxPalCenterID   C   R
1     #      0       0      -1         0            0       0        1          1   1 
2     a      1       1       0         1            0       1        2          2   3 
3     #      2       3       1         2            0       0        2          2   3 
4     f      2       3       0         2            0       3        4          4   7 
5     #      4       7       3         4            0       0        4          4   7 
6     a      4       7       2         4            0       1        4          4   7 
for i = 6, something happened. We know R > i. This means we are part of a previous palindrome. 
So now instead of checking every single character on either side of i = 6, we can make a leap. 
This is saying that hey, I saw a palindrome with center i = 2 and I can use that to my advantage. 
We use the minimum of R-i or P[ii]. Why? We know that R is the right edge of some palindrome. 
However, there could be a shorter palindrome. Hence take the min

to better illustrate, consider string "abababababa" --> "^#a#b#a#b#a#b#a#b#a#b#a#$"
# a # b # a # b #  a  #  b  #  a  #  b  #  a  #  b  #  a  # $
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

For i = 5, we are at the third #. Even though we know that a palindrom at b (i = 4) as 
in #a#b#a# has a right edge of 7, we have to compare every character since min(R-i, P[ii]) = P[ii]. 

However for i = 14, we know the stuff to the right of i = 14 is part of a larger palindrome 
starting at i = 12. so we start the comparisons from R+i - P[i] = 24. 

Where did ii = 2C - i come from? 
The center is always to the left of i. 
So for some C and i > C, i - C tells the distance of where we are with respect to C
The index on the left side of C that is equally distant from C is C - (i-C) = 2C - i
'''

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
    n = len(t)
    P = [0]*n
    i = 1

    maxPalCenterID = 1
    C = R = 0

    while i < n-1:
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


longestPalindrome("afabcabaabcde")
