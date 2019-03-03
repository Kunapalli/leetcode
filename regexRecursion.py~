def isMatch(s, p):
    return isMatch2(s, p, 0, 0)


def isMatch2(s, p, si, pi):
    if pi == len(p) and si < len(s):
        return False

    if si == len(s):
        if pi == len(p):
            return True
        else:
            incs = pi < len(p) - 1 and p[pi+1] == '*'  # is Next Char Star 
            return incs and isMatch2(s, p, si, pi + 2)

    hfcm = (s[si] == p[pi] or p[pi] == '.')      # has first char matched
    incs = (pi < len(p) - 1 and p[pi+1] == '*')  # is next char star

    # suppose s1 = aabb, s2 = bb and p = a*b*. We don't know whether our string s is like s1 or s2.
    # so we have two possibilities.
    # 1. we assume a* matches null as in s2. Then compare s2 with p+2
    # 2. a* matches sequence of a as in s1. Then compare s1+1 with p
    if incs:
        r = isMatch2(s, p, si, pi + 2) # assumes char* matches null
        if hfcm:
            x = isMatch2(s, p, si + 1, pi) # assumes char* matches an a and try again
            r = r or x
        return r

    # if we are here, we just check to see if firs char matched and then compare s+1 and p+1
    return hfcm and isMatch2(s, p, si + 1, pi + 1) 

    

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
