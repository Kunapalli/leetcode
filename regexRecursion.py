def isMatch(s, p):
    return isMatch2(s, p, 0, 0)


def isMatch2(s, p, si, pi):
    if pi == len(p) and si < len(s): # if pattern ended but string left over, false
        return False

    if si == len(s): # if pattern and string finish, true
        if pi == len(p):
            return True
        else: # string is done but pattern left over. This means the rest of the pattern should be 
            # one or more char* (these will match null)
            # example: s = aabb, p = a*b*c*d*
            # if we came here, s is done and p = c*d* we need to check every other char is a '*'
            incs = pi < len(p) - 1 and p[pi+1] == '*'  # is Next Char Star 
            return incs and isMatch2(s, p, si, pi + 2)

    hfcm = (s[si] == p[pi] or p[pi] == '.')      # has first char matched
    incs = (pi < len(p) - 1 and p[pi+1] == '*')  # is next char star

    # suppose s1 = aabb, s2 = bb and p = a*b*. We don't know whether our string s is like s1 or s2.
    # so we have two possibilities.
    # 1. we assume a* matches null as in s2. Then compare s with p+2
    # 2. a* matches first a in s1. Then compare s+1 with p
    if incs:
        r = isMatch2(s, p, si, pi + 2) # assumes char* matches null
        if hfcm:
            x = isMatch2(s, p, si + 1, pi) # assumes char* matches an a and try again
            r = r or x
        return r

    # if we are here, we just check to see if first char matched and then compare s+1 and p+1
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
