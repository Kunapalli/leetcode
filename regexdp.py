# https://leetcode.com/problems/regular-expression-matching/
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''
def isMatch(s, p):
    # what does dp contain?
    # dp[pi][si] is True if pattern ending just before pi matches string ending just before si
    # which is exactly why dp[-1][-1] holds the final answer

    dp = [[False,]*(len(s)+1) for i in range(len(p)+1)]
    dp[0][0] = True

    # why is the below for loop needed?
    # it is because the pattern a*b*c could match just c. Hence we start with p[2][0] = True and
    # similarly p[4][0] = True

    for i in range(1,len(p)+1):
        if p[i-1] == '*':
            dp[i][0] = dp[i-2][0]

    # We start for the first character of both s and p.
    # Now if the prev char of p is a '*', then:
    #       there is possibility for this to be empty match. So we assign dp[pi][si] = dp[pi-2][si]
    #       now if the first char matched, then this is not an empty match. so we or the value with dp[pi][si-1]
    #     else
    #        check if the prev char in p and s are equal and 'and' that with dp[pi-1][si-1]

    for pi in range(1, len(p) + 1):
        for si in range(1, len(s) + 1):
            if p[pi-1] == '*':
                # two possibilities just as in the recursion solution. Either char* matches null or not.
                # option 1: assume char* matches null. So the pattern ending just before pi-2
                # matches string ending in si. OR
                # option 2: asume char* does not match null.
                #      if p-2 matches s-1, use whatever is in dp[pi][si-1]
                dp[pi][si] = dp[pi-2][si] or ((s[si-1] == p[pi-2] or p[pi-2] == '.') and dp[pi][si-1])
            else:
                # pattern not char*, so check if prev chars are equal and look at p-1,s-1
                dp[pi][si] = (s[si-1] == p[pi-1] or p[pi-1] == '.') and dp[pi-1][si-1]

    return dp[-1][-1]


print(isMatch("aa", "a*b*c*")) # True
print(isMatch("a", ".")) # True
print(isMatch("a", "..")) # False
print(isMatch("a", ".*")) # True
print(isMatch("aa", "ab")) # False
print(isMatch("aaaa", ".*")) # True
print(isMatch("aaaa", ".")) # False
print(isMatch("aaaa", "**")) # False 
print(isMatch("aab", "c*a*b")) # True
print(isMatch("mississippi", "mis*is*p*.")) # False (there is no match for third 'i')
